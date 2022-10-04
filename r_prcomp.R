install.packages("HSAUR2")
library(HSAUR2)
data(heptathlon)
head(heptathlon)    
write.csv(heptathlon, file="c:/data/pydata/heptathlon.csv")
heptathlon$hurdles = max(heptathlon$hurdles) - heptathlon$hurdles
heptathlon$run200m = max(heptathlon$run200m) - heptathlon$run200m
heptathlon$run800m = max(heptathlon$run800m) - heptathlon$run800m

hep_data = heptathlon[, -8]
# Principal component analysis using prcomp (using SVD)
hep_pca =  prcomp(hep_data, scale=TRUE)
names(hep_pca)
help(‘prcomp’)
summary(hep_pca)   
eig_val = hep_pca$sdev^2
round(eig_val, 3)
# [1] 4.460 1.194 0.521 0.457 0.245 0.073 0.049
round(cumsum(eig_val),3)
# [1] 4.460 5.655 6.176 6.633 6.878 6.951 7.000
