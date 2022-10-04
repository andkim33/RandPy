library(reticulate)
py_install(packages="pandas", "scikit-learn")

# Ex-1
source_python("c:/rpy2_pgm/py_read.txt")
flights <- read_flights("c:/data/pydata/flights.csv")
head(flights,3)
library(ggplot2)
ggplot(flights, aes(carrier, arr_delay)) + geom_point() + geom_jitter()

# Ex-2
# Ex-2
data(mtcars)
py_desc(mtcars)     

# Ex-3
reg_py$fit(X = mtcars[,-1], y = mtcars$mpg)
data.frame(var = c("Intercept", names(mtcars)[-1]), 
           python_coef = c(reg_py$intercept_, reg_py$coef_))

#         var python_coef
#1  Intercept 12.30337416
#2        cyl -0.11144048
#3       disp  0.01333524
#4         hp -0.02148212
#5       drat  0.78711097
#6         wt -3.71530393
#7       qsec  0.82104075
#8         vs  0.31776281
#9         am  2.52022689
#10      gear  0.65541302
#11      carb –0.19941925

# Fit lm in R 
fit =  lm(mpg ~ ., data = mtcars)
data.frame(R_coef = coef(fit))
