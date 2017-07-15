## 3. Introduction to the Data ##

import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")

print(all_ages.head(5))
print(recent_grads.head(5))

## 4. Summarizing Major Categories ##

# Unique values in Major_category column.
#print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()

rg_cat_unique = recent_grads['Major_category'].unique()
for val in rg_cat_unique:
    rows_rg_cat_unique = recent_grads[recent_grads['Major_category']==val]
    rg_sum = rows_rg_cat_unique['Total'].sum()
    rg_cat_counts[val] = rg_sum

aa_cat_unique = all_ages['Major_category'].unique()
for val in rg_cat_unique:
    rows_aa_cat_unique = all_ages[all_ages['Major_category']==val]
    aa_sum = rows_aa_cat_unique['Total'].sum()
    aa_cat_counts[val] = aa_sum

## 5. Low-Wage Job Rates ##

import numpy as np
low_wage_percent = 0.0
low_wage = recent_grads.pivot_table(index = 'Low_wage_jobs', values = 'Total', aggfunc= np.sum)
total = recent_grads['Total'].sum()
low_wage_percent = low_wage/total
print(low_wage_percent)

## 6. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0
for val in majors:
    rows_rg = recent_grads[recent_grads['Major']==val]
    rows_aa = all_ages[all_ages['Major']==val]
    if(rows_rg['Unemployment_rate'].sum() < rows_aa['Unemployment_rate'].sum()):
        rg_lower_count = rg_lower_count+1
print(rg_lower_count)