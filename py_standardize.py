# Python : Data Scaling

# part 1 : Scale test data using (test data, only results of scaling train data) 

def ZScaler(data) :
    from sklearn.preprocessing import StandardScaler
    z = StandardScaler()
    z.fit(data)
    zdata = z.transform(data)
    n = z.n_samples_seen_
    zdata = zdata * np.sqrt((n-1)/n)
    return zdata, z, n


def ZScaler_test(test_data, zfit_train, n_train) :
    zdata = zfit_train.transform(test_data)
    n = n_train
    zdata = zdata * np.sqrt((n-1)/n)
    return zdata

def MinMaxScaler(data) :
    from sklearn.preprocessing import MinMaxScaler
    zm = MinMaxScaler()
    zm.fit(data)
    MinMaxData = zm.transform(data)
    return MinMaxData, zm

def MinMaxScaler_test(test_data, zm) :
    MinMaxData = zm.transform(test_data)
    return MinMaxData

# part 2: Scale test data using (train data, test data)

def ZScaler2(data) :
    from sklearn.preprocessing import StandardScaler
    z = StandardScaler()
    z.fit(data)
    zdata = z.transform(data)
    n = z.n_samples_seen_
    zdata = zdata * np.sqrt((n-1)/n)
    return zdata

def ZScaler_test2(train_data, test_data) :
    from sklearn.preprocessing import StandardScaler
    z = StandardScaler()
    z.fit(train_data)
    zdata = z.transform(test_data)
    n = z.n_samples_seen_
    zdata = zdata * np.sqrt((n-1)/n)
    return zdata



def MinMaxScaler2(data) :
    from sklearn.preprocessing import MinMaxScaler
    zm = MinMaxScaler()
    zm.fit(data)
    MinMaxData = zm.transform(data)
    return MinMaxData

def MinMaxScaler_test2(train_data, test_data) :
    from sklearn.preprocessing import MinMaxScaler
    zm = MinMaxScaler()
    zm.fit(train_data)
    MinMaxData = zm.transform(test_data)
    return MinMaxData


from sklearn.model_selection import train_test_split
from sklearn import datasets 
import numpy as np
import pandas as pd

iris = datasets.load_iris()
# iris : Bunch object (like dictionaries)
iris.keys()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
     X, y, train_size=0.7, random_state=12345)
X_train.shape  
X_test.shape


ZX_train, zfit_train, n_train = ZScaler(X_train)
ZX_test = ZScaler_test(X_test, zfit_train, n_train)

ZX_train2 = ZScaler2(X_train) 
ZX_test2 = ZScaler_test2(X_train, X_test) 

Z01_train, z01_fit = MinMaxScaler(X_train)
Z01_test = MinMaxScaler_test(X_test, z01_fit)

Z01_train2 = MinMaxScaler2(X_train)
Z01_test2 = MinMaxScaler_test2(X_train, X_test)

Z01_TR = pd.DataFrame(Z01_train)
Z01_TR2 = pd.DataFrame(Z01_train2)
Z01_TE = pd.DataFrame(Z01_test)
Z01_TE2 = pd.DataFrame(Z01_test2)
Z01_TR.head()
Z01_TR2.head()
Z01_TE.head()
Z01_TE2.head()
Z01_TR.describe()
Z01_TR2.describe()
Z01_TE.describe()
Z01_TE2.describe()

