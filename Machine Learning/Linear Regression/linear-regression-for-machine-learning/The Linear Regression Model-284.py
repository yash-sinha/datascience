## 2. Introduction To The Data ##

import pandas as pd
data = pd.read_csv("AmesHousing.txt", sep='\t')
train = data.iloc[0:1460]
test = data.iloc[1460:]
data.info()
target = "SalePrice"


## 3. Simple Linear Regression ##

import matplotlib.pyplot as plt
# For prettier plots.
import seaborn as sns
sns.regplot(train["Garage Area"], train["SalePrice"], scatter = True)
sns.regplot(train["Gr Liv Area"], train["SalePrice"], scatter = True)
sns.regplot(train["Overall Cond"], train["SalePrice"], scatter = True)



## 5. Using Scikit-Learn To Train And Predict ##

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(train[["Gr Liv Area"]], train["SalePrice"])
a0 = model.intercept_
a1 = model.coef_

## 6. Making Predictions ##

import numpy as np
from sklearn.metrics import mean_squared_error
import math
lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])
predict_train = lr.predict(train[["Gr Liv Area"]])
predict_test = lr.predict(test[["Gr Liv Area"]])

train_rmse = math.sqrt(mean_squared_error(train["SalePrice"], predict_train))
test_rmse = math.sqrt(mean_squared_error(test["SalePrice"], predict_test))

## 7. Multiple Linear Regression ##

import math
cols = ['Overall Cond', 'Gr Liv Area']
model = LinearRegression()
target = "SalePrice"
model.fit(train[cols], train[target])
predict_train = model.predict(train[cols])
predict_test = model.predict(test[cols])

train_rmse_2 = math.sqrt(mean_squared_error(train[target], predict_train))
test_rmse_2 = math.sqrt(mean_squared_error(test[target], predict_test))