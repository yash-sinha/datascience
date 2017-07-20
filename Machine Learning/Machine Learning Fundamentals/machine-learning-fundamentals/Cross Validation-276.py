## 1. Introduction ##

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

#Shuffle
np.random.seed(1)
shuffled = np.random.permutation(len(dc_listings))
dc_listings = dc_listings.loc[shuffled]
split_one = dc_listings.iloc[0:1862]
split_two = dc_listings.iloc[1862:]
print(len(split_one))

## 2. Holdout Validation ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import math
train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

knn = KNeighborsRegressor(n_neighbors = 5)
knn.fit(train_one[["accommodates"]], train_one["price"])
predictions = knn.predict(test_one[["accommodates"]])
iteration_one_rmse = math.sqrt(mean_squared_error(test_one["price"], predictions))

knn.fit(train_two[["accommodates"]], train_two["price"])
predictions = knn.predict(test_two[["accommodates"]])
iteration_two_rmse = math.sqrt(mean_squared_error(test_two["price"], predictions))

avg_rmse = np.mean([iteration_one_rmse, iteration_two_rmse])

## 3. K-Fold Cross Validation ##

dc_listings.set_value(dc_listings.index[0:744], "fold", 1)
dc_listings.set_value(dc_listings.index[744:1488], "fold", 2)
dc_listings.set_value(dc_listings.index[1488:2232], "fold", 3)
dc_listings.set_value(dc_listings.index[2232:2976], "fold", 4)
dc_listings.set_value(dc_listings.index[2976:3723], "fold", 5)

## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import math
train_set = dc_listings[ dc_listings["fold"] != 1]
test_set = dc_listings[dc_listings["fold"] == 1]
knn = KNeighborsRegressor()
knn.fit(train_set[["accommodates"]], train_set["price"])
labels = knn.predict(test_set[["accommodates"]])

iteration_one_rmse = math.sqrt(mean_squared_error(test_set["price"], labels))
                 

## 5. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
import math
fold_ids = [1,2,3,4,5]
rmses = []
def train_and_validate(df, fold):
    train_set = df[ df["fold"] != fold]
    test_set = df[df["fold"] == fold]
    knn = KNeighborsRegressor()
    knn.fit(train_set[["accommodates"]], train_set["price"])
    labels = knn.predict(test_set[["accommodates"]])
    rmses.append(math.sqrt(mean_squared_error(test_set["price"], labels)))
    
for fold in fold_ids:
    train_and_validate(dc_listings, fold)

avg_rmse = sum(rmses)/len(rmses)



## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
import math
kf = KFold(n = len(dc_listings), n_folds = 5, shuffle = True, random_state = 1)

knn = KNeighborsRegressor()
mses = cross_val_score(knn, dc_listings[["accommodates"]], dc_listings["price"], scoring="mean_squared_error", cv = kf)
rmses = [np.sqrt(np.absolute(mse)) for mse in mses]
avg_rmse = np.mean(rmses)

print(rmses)
print(avg_rmse)

## 7. Exploring Different K Values ##

from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
num_folds = [3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 21, 23]

for fold in num_folds:
    kf = KFold(len(dc_listings), fold, shuffle=True, random_state=1)
    model = KNeighborsRegressor()
    mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="mean_squared_error", cv=kf)
    rmses = [np.sqrt(np.absolute(mse)) for mse in mses]
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    print(str(fold), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))