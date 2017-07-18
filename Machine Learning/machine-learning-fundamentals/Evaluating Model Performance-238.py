## 1. Testing quality of predictions ##

import pandas as pd
import numpy as np
dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
train_df = dc_listings.iloc[0:2792]
test_df = dc_listings.iloc[2792:]

def predict_price(new_listing):
    temp_df = train_df
    temp_df['distance'] = temp_df['accommodates'].apply(lambda x: np.abs(x - new_listing))
    temp_df = temp_df.sort_values('distance')
    nearest_neighbor_prices = temp_df.iloc[0:5]['price']
    predicted_price = nearest_neighbor_prices.mean()
    return(predicted_price)

test_df["predicted_price"] = test_df["accommodates"].apply(predict_price)

## 2. Error Metrics ##

import numpy as np
mae = abs(test_df["predicted_price"] - test_df["price"]).mean()

## 3. Mean Squared Error ##

mse = pow(test_df["predicted_price"] - test_df["price"], 2).mean()

## 4. Training another model ##

train_df = dc_listings.iloc[0:2792]
test_df = dc_listings.iloc[2792:]

def predict_price(new_listing):
    temp_df = train_df
    temp_df['distance'] = temp_df['bathrooms'].apply(lambda x: np.abs(x - new_listing))
    temp_df = temp_df.sort_values('distance')
    nearest_neighbors_prices = temp_df.iloc[0:5]['price']
    predicted_price = nearest_neighbors_prices.mean()
    return(predicted_price)

test_df["predicted_price"] = test_df["bathrooms"].apply(predict_price)
mse = pow(test_df["predicted_price"] - test_df["price"], 2).mean()
print(mse)

## 5. Root Mean Squared Error ##

import math
def predict_price(new_listing):
    temp_df = train_df
    temp_df['distance'] = temp_df['bathrooms'].apply(lambda x: np.abs(x - new_listing))
    temp_df = temp_df.sort_values('distance')
    nearest_neighbors_prices = temp_df.iloc[0:5]['price']
    predicted_price = nearest_neighbors_prices.mean()
    return(predicted_price)

test_df['predicted_price'] = test_df['bathrooms'].apply(lambda x: predict_price(x))
test_df['squared_error'] = (test_df['predicted_price'] - test_df['price'])**(2)
mse = test_df['squared_error'].mean()
rmse = math.sqrt(mse)

## 6. Comparing MAE and RMSE ##

import math
errors_one = pd.Series([5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10])
errors_two = pd.Series([5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 1000])
mae_one = sum(errors_one)/ len(errors_one)
mae_two = sum(errors_two)/ len(errors_two)
#sum(map(lambda x: x**2,(errors_one)))
rmse_one = math.sqrt((errors_one**2).sum()/ len(errors_one))
rmse_two = math.sqrt((errors_two**2).sum()/ len(errors_two))