"""
Before Python, you should run the following scripts in R .
(file : r_iris_save.txt)

data(iris)
names(iris) = c("SL","SW","PL","PW","SP")
levels(iris$SP) = c("st","vc","vg")
write.csv(iris, file=’d:/rpy/niris.csv’)

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# pip install tensorflow, 
# pip install keras

import tensorflow as tf
import keras
import pandas as pd
iris=pd.read_csv('d:/rpy/niris.csv')
iris["SP"] = iris["SP"].astype("category").cat.codes
X=iris.iloc[:,1:-1]
y=iris["SP"]
Y = tf.keras.utils.to_categorical(y, num_classes=3)

# train test split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30)
X_train.shape

# Scale data to have mean 0 and variance 1 in X_train
# Modified Standardization  
ZX_train, zfit_train, n_train = ZScaler(X_train)
ZX_test = ZScaler_test(X_test, zfit_train, n_train)

from keras.models import Sequential
from keras.layers import Dense
model_1 = Sequential()
model_1.add(Dense(8, input_dim=4, activation='relu'))
model_1.add(Dense(3, activation='softmax'))
model_1.compile(loss='categorical_crossentropy', 
                      optimizer='adam', 
                      metrics=['accuracy'])
model_1.summary()
model_1.fit(zX_train, Y_train, batch_size=5, epochs=50)
_, accuracy = model_1.evaluate(ZX_train, Y_train)
print('Accuracy: %.2f' % (accuracy*100))
Accuracy: 89.52

_, accuracy = model_1.evaluate(ZX_test, Y_test)
2/2 [==============================] - 0s 2ms/step - loss: 0.3796 - accuracy: 0.8444
print('Accuracy: %.2f' % (accuracy*100))
Accuracy: 84.44

prediction = model_1.predict(ZX_test)
prediction_ = np.argmax(prediction, axis = 1)
Y_test_target = np.argmax(Y_test, axis=1)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(Y_test_target, prediction_))
[[17  0  0]
 [ 0 13  5]
 [ 0  2  8]]

print(classification_report(Y_test_target, prediction_))
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        17
           1       0.87      0.72      0.79        18
           2       0.62      0.80      0.70        10

    accuracy                           0.84        45
   macro avg       0.83      0.84      0.83        45
weighted avg       0.86      0.84      0.85        45
