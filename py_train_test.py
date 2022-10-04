from sklearn.model_selection import train_test_split
from sklearn import datasets 
iris = datasets.load_iris()
# iris : Bunch object (like dictionaries)
iris.keys()

X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
     X, y, train_size=0.7, random_state=12345)
X_train.shape()  
X_test.shape()