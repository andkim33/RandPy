 devtools::install_github("rstudio/keras")
 library(keras)
 install_keras()
 data(iris)
 iris_data <- iris
 names(iris_data) = c("SL","SW","PL","PW","SP")
 levels(iris_data$SP) = c("st","vc","vg")

 # iris species (setosa, versicolor, virginica) -> (1,2,3)
 iris_data[,5] <- as.numeric(as.factor(unlist(iris_data[,5])))  - 1
 # dataframe -> matrix 
 iris_data <- as.matrix(iris_data)
 dimnames(iris_data) <- NULL

 # Split iris_data into train and test data 
 samp= c(sample(1:50, 35), sample(51:100, 35), sample(101:150, 35))
 iris_train_X = iris_data[samp, -5]   # train data
 iris_test_X = iris_data[-samp, -5]   # test data
 iris_train_target = iris_data[samp, 5]
 iris_test_target = iris_data[-samp, 5]
 iris_train_labels = to_categorical(iris_train_target)
 iris_test_labels = to_categorical(iris_test_target)

 # MinMax Scaling for train data
 ziris_train = RStandardization(iris_train_X, method="minmax") 
 ztrain_data = ziris_train$data
 ztrain_center = ziris_train$center
 ztrain_scale = ziris_train$scale

 set.seed(12345)
 iris_model = keras_model_sequential()
 iris_model %>%
   layer_dense(units=8, activation="relu", input_shape=c(4)) %>%
   layer_dense(units=3, activation="softmax")
 summary(iris_model)
 iris_model %>% compile(
   loss='categorical_crossentropy', optimizer='adam', metrics='accuracy')
 iris_model %>% fit ( 
   ziris_train_X, iris_train_labels, epoch=500, batch_size=5, validation_split=0.1)
 
# Predict iris_test_Xsing ziris_test_X
 ziris_test_X = RStandardization_test(iris_test_X, ztrain_center, ztrain_scale)

 test_pred_class = iris_model %>% predict(ziris_test_X, batch_size=150)
 test_pred_class
 iris_test_target
 score = iris_model %>% evaluate(ziris_test_X, iris_test_labels, batch_size=150)
 print(score)
 iris_pred_target = apply(test_pred_class, 1, which.max)
 iris_pred_target = iris_pred_target – 1
 iris_pred_target
 [1] 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2  
    2 2 2 2 2 2
  table(iris_test_target, iris_pred_target)
#                  iris_pred_target
# iris_test_target     0  1  2
                    0 15  0  0
                    1  0 14  1
                    2  0  1 14
