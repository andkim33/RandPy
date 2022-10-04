import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#데이터 읽기
heptathlon = pd.read_csv("c:/data/pydata/heptathlon.csv")
heptathlon.head(3)
# 변수이름 확인하기
heptathlon.columns
# 변환: 변수최댓값 - 변숫값
heptathlon.hurdles = np.max(heptathlon.hurdles) - heptathlon.hurdles
heptathlon.run200m = np.max(heptathlon.run200m) - heptathlon.run200m
heptathlon.run800m = np.max(heptathlon.run800m) - heptathlon.run800m
# 분석변수 선택하기
hep_data = heptathlon.iloc[:, 1:-1]
# 변수 표준화 – 기존 이용
from sklearn.preprocessing import StandardScaler
zx = StandardScaler().fit_transform(hep_data)
# 초기 주성분분석
from sklearn.decomposition import PCA
help(PCA)
pca_init = PCA(n_components=len(hep_data.columns))
pca_init.fit(zx)
# pca_init.explained_variance_
np.round(pca_init.explained_variance_, 3)
# Out[11]: array([4.646, 1.244, 0.543, 0.476, 0.255, 0.076, 0.051])
# np.cumsum(pca_init.explained_variance_)
np.round(np.cumsum(pca_init.explained_variance_), 3)
# Out[14]: array([4.646, 5.89 , 6.433, 6.909, 7.165, 7.241, 7.292])


RStandardization = function(data, method=“zscore”)
{
    if(method != “zscore”) method = “minmax”
    if(method = “zscore”)
       zdata = scale(data, center=TRUE, scale=TRUE)    
    else if(method = “minmax”)
       {
            # 0-1 transformation
            maxX = apply(data, 2, max)
            minX = apply(data, 2, min)   
            zdata = scale(data, center=minX, scale=maxX – minX)
        }
     return(zdata)
}

def ZScaler(data) :
    from sklearn.preprocessing import StandardScaler
    z = StandardScaler()
    z.fit(data)
    zdata = z.transform(data)
    n = z.n_samples_seen_
    zdata = zdata * np.sqrt((n-1)/n)
    return zdata

# 변수 표준화 – 새로운 함수 이용
zx2, _, _ = ZScaler(hep_data)
# 초기 주성분분석
from sklearn.decomposition import PCA
pca2_init = PCA(n_components=len(hep_data.columns))
pca2_init.fit(zx2)
np.round(pca2_init.explained_variance_, 3)
# Out[19]: array([4.46 , 1.194, 0.521, 0.457, 0.245, 0.073, 0.049])
np.round(np.cumsum(pca2_init.explained_variance_), 3)
# Out[21]: array([4.46 , 5.655, 6.176, 6.633, 6.878, 6.951, 7.   ])
