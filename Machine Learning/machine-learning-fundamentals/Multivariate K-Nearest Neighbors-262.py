## 1. Recap ##

import pandas as pd
import numpy as np
np.random.seed(1)

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings.info()

## 2. Removing features ##

cols = ["room_type", "city", "state", "latitude", "longitude", "zipcode", "host_response_rate", "host_acceptance_rate", "host_listings_count"]
dc_listings.drop(labels = cols, axis = 1, inplace = True)

## 3. Handling missing values ##

cols = ["cleaning_fee", "security_deposit"]
dc_listings.drop(labels = cols, axis = 1, inplace = True)
cols = ["bedrooms", "beds", "bathrooms"]
dc_listings.dropna(subset = cols ,axis=0, inplace = True)
#dc_listings.info()
print(dc_listings.isnull().sum())

## 4. Normalize columns ##

normalized_listings = (dc_listings - dc_listings.mean()) / (dc_listings.std())
normalized_listings["price"] = dc_listings["price"]
normalized_listings.head(3)

## 5. Euclidean distance for multivariate case ##

from scipy.spatial import distance
first_fifth_distance = distance.euclidean(normalized_listings.iloc[0][['accommodates', 'bathrooms']], normalized_listings.iloc[4][['accommodates', 'bathrooms']])

print(first_fifth_distance)

## 7. Fitting a model and making predictions ##

from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(algorithm = "brute")
train_df = normalized_listings.iloc[0:2792]
test_df = normalized_listings.iloc[2792:]
train_features = train_df[['accommodates', 'bathrooms']]
train_target = train_df['price']
knn.fit(train_features, train_target)
predictions = knn.predict(test_df[['accommodates', 'bathrooms']])



## 8. Calculating MSE using Scikit-Learn ##

from sklearn.metrics import mean_squared_error
import math
train_columns = ['accommodates', 'bathrooms']
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute', metric='euclidean')
knn.fit(train_df[train_columns], train_df['price'])
predictions = knn.predict(test_df[train_columns])

two_features_mse = mean_squared_error(test_df['price'], predictions)
two_features_rmse = math.sqrt(two_features_mse)


## 9. Using more features ##

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
from sklearn.neighbors import KNeighborsRegressor
import math
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')
knn.fit(train_df[features], train_df["price"])
four_predictions = knn.predict(test_df[features])

four_mse = mean_squared_error(test_df["price"], four_predictions)
four_rmse = math.sqrt(four_mse)

## 10. Using all features ##

import math
all_cols = train_df.columns
cols = []
for col in all_cols:
    if col == "price":
        continue
    else:
        cols.append(col)
knn.fit(train_df[cols], train_df["price"])
all_features_predictions= knn.predict(test_df[cols])

all_features_mse = mean_squared_error(test_df["price"], all_features_predictions)
all_features_rmse = math.sqrt(all_features_mse)