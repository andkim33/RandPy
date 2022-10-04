RStandardization = function(data, method="zscore")
{
    if(method == "zscore") 
    {
            center_value = apply(data, 2, mean, na.rm = TRUE)     
            scale_value = apply(data, 2, sd, na.rm = TRUE)
            ### zdata = scale(data, center=TRUE, scale= TRUE) 
            zdata = scale(data, center=center_value, scale= scale_value)    
               
    }
    else if(method == "minmax")
       {
            # 0-1 transformation
            maxX = apply(data, 2, max)
            minX = apply(data, 2, min)
            center_value = minX
            scale_value = maxX - minX
            zdata = scale(data, center=center_value, scale= scale_value)   
      }
 
   zdata_value = list(zdata = zdata, center = center_value, scale = scale_value) 
   return(zdata_value)
}


RStandardization_test = function(test_data, center_value, scale_value)
{
       zdata_test = scale(test_data, center=center_value, scale=scale_value)
       return(zdata_test)
}

RStandardization2 = function(data, method="zscore")
{
    if(method == "zscore")
       zdata = scale(data, center=TRUE, scale=TRUE)    
    else if(method == "minmax")
       {
            # 0-1 transformation
            maxX = apply(data, 2, max)
            minX = apply(data, 2, min)
            maxmin = maxX - minX
            zdata = scale(data, center=minX, scale=maxmin )
      }
  
   return(zdata)
}


RStandardization2_test = function(train_data, test_data, method="zscore")
 {
    if(method == "zscore")
     {
       zX_mean = apply(train_data, 2, mean, na.rm = TRUE)     
       zX_sd = apply(train_data, 2, sd, na.rm = TRUE)
       zdata_test = scale(test_data, center=zX_mean, scale=zX_sd)
      }
    else if(method == "minmax")
    {
    # 0-1 transformation
     maxX = apply(train_data, 2, max)
     minX = apply(train_data, 2, min)   
     maxmin = maxX - minX
     zdata_test = scale(test_data, center=minX, scale=maxmin )
    }

    return(zdata_test)
}

data(iris)
train_test = Train_Test_Split_m1(iris, SplitRatio=0.8)
train_data = train_test$train_data
test_data = train_test$test_data
X_train = train_data[, -5]
y_train = train_data[, 5]
X_test = test_data[, -5]
y_test = test_data[, 5]

ztrain  =  RStandardization(X_train, method="zscore")
ztrain_data = ztrain$data
ztrain_center = ztrain$center
ztrain_scale = ztrain$scale

ztest_data = RStandardization_test(X_test, ztrain_center, ztrain_scale)
ztest2_data = RStandardization2_test(train, test, method="zscore")

head(ztest_data)
head(ztest2_data)


