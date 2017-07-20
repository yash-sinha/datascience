## 1. Missing Values ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]
numerical_train = train.select_dtypes(include=['int', 'float'])
cols = ["PID","Year Built","Year Remod/Add", "Garage Yr Blt", "Mo Sold", "Yr Sold"]
numerical_train.drop(labels = cols, axis = 1, inplace = True)
null_series = numerical_train.isnull().sum()
full_cols_series = null_series[null_series == 0]
print(full_cols_series)


## 2. Correlating Feature Columns With Target Column ##

train_subset = train[full_cols_series.index]
corrs = train_subset.corr()

sorted_corrs = abs(corrs["SalePrice"]).sort_values()

## 3. Correlation Matrix Heatmap ##

import seaborn as sns
import matplotlib.pyplot as plt 
plt.figure(figsize=(10,6))
strong_corrs = sorted_corrs[sorted_corrs > 0.3]
corrmat = train_subset[strong_corrs.index].corr()
sns.heatmap(corrmat)

## 4. Train And Test Model ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import math
final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'
clean_test = test[final_corr_cols.index].dropna()

model = LinearRegression()
model.fit(train[features], train[target])
predictions_train  = model.predict(train[features])
predictions_test  = model.predict(clean_test[features])

train_rmse = math.sqrt(mean_squared_error(predictions_train, train["SalePrice"]))
test_rmse = math.sqrt(mean_squared_error(predictions_test, clean_test["SalePrice"]))


## 5. Removing Low Variance Features ##

normalized_train = train[features]/(train[features].max())
sorted_vars = normalized_train.var().sort_values()
print(sorted_vars)

## 6. Final Model ##

features = features.drop("Open Porch SF")
model = LinearRegression()
model.fit(train[features], train[target])
predictions_train  = model.predict(train[features])
predictions_test  = model.predict(clean_test[features])

train_rmse_2 = math.sqrt(mean_squared_error(predictions_train, train["SalePrice"]))
test_rmse_2 = math.sqrt(mean_squared_error(predictions_test, clean_test["SalePrice"]))
