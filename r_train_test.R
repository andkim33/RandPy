Train_Test_Split_m1 = function(data, SplitRatio = 0.7) 
 {
   # set.seed(12345)
   split_size = round(nrow(data)*SplitRatio) 
   train_id = sample(c(1:nrow(data)), size=split_size)
   train_data = data[train_id,]
   test_data = data[-train_id,]
   result = list(train_data = train_data, test_data=test_data)
   return(result)
 }


Train_Test_Split_m2 = function(data, SplitRatio = 0.7) 
 {
    require(dplyr)
    library(dplyr)
    data$id <- 1:nrow(data)
    # set.seed(34567) 
    train_data <- data %>% dplyr::sample_frac(SplitRatio)
    test_data  <- dplyr::anti_join(data, train, by = 'id')
    result = list(train_data = train_data, test_data=test_data)
    return(result)
}


data(iris)
train_test = Train_Test_Split_m1(iris, SplitRatio=0.6)
train = dim(train_test$train_data
dim(train)
test = dim(train_test$test_data
dim(test)


data(iris)
train_test2 = Train_Test_Split_m2(iris) 
train_data2 = train_test2$train_data
test_data2 = train_test2$test_data
dim(train_data2)
dim(test_data2)

