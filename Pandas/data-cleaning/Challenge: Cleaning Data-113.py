## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers["Year"] > 1960]

## 5. Consolidating Deaths ##

deaths = ["Death2", "Death3","Death4", "Death5"]
def add_deaths(inp):
    if pd.isnull(inp) or inp == "NO":
        return 0
    elif inp == "YES":
        return 1
true_avengers["Deaths"] = true_avengers["Death1"].apply(add_deaths)
for death in deaths:
    true_avengers["Deaths"] += true_avengers[death].apply(add_deaths)

## 6. Verifying Years Since Joining ##

correct = true_avengers[2015 - true_avengers["Year"] == true_avengers["Years since joining"]]
joined_accuracy_count  = int(correct.shape[0])
