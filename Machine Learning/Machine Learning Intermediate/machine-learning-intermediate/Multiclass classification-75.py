## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")

unique_regions = cars["origin"].unique()

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)

dummy_year = pd.get_dummies(cars["year"], prefix = "year")
cars = pd.concat([cars, dummy_year], axis =1)

cars.drop(["year", "cylinders"], axis =1, inplace = True)

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]
length = int(len(shuffled_cars) * 0.7)
train = shuffled_cars[:length]
test = shuffled_cars[length:]

## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}

for unique in unique_origins:
    X = cars.filter(regex=("(year|cyl|)*"))
    y = cars["origin"] == unique
    model = LogisticRegression()
    model.fit(X,y)
    models[unique] = model

## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)
features = [c for c in train.columns if c.startswith("cyl") or c.startswith("year")]
for unique in unique_origins:
    X = test[features]
    testing_probs[unique] = models[unique].predict_proba(X)[:,1]
   

## 6. Choose the origin ##

predicted_origins = testing_probs.idxmax(axis = 1)