## 3. Converting Categorical Variables ##

# Convert a single column from text categories to numbers
import pandas as pd
col = pd.Categorical.from_array(income["workclass"])
income["workclass"] = col.codes
print(income["workclass"].head(5))

cols = ["education", "marital_status", "occupation", "relationship", "race", "sex", "native_country", "high_income"]

for col in cols:
    num =  pd.Categorical.from_array(income[col])
    income[col] = num.codes

## 5. Creating Splits ##

private_incomes = income[income["workclass"] == 4]
public_incomes = income[income["workclass"] !=4 ]

## 9. Overview of Data Set Entropy ##

import math
# We'll do the same calculation we did above, but in Python
# Passing in 2 as the second parameter to math.log will take a base 2 log
num_1 = len(income[income["high_income"] == 1])
num_0 = income.shape[0] - num_1
total = income.shape[0]
income_entropy = -(num_1/total * math.log(num_1/total, 2) + num_0/total * math.log(num_0/total, 2))

## 11. Information Gain ##

import numpy

def calc_entropy(column):
    """
    Calculate entropy given a pandas series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column
    counts = numpy.bincount(column)
    # Divide by the total column length to get a probability
    probabilities = counts / len(column)
    
    # Initialize the entropy to 0
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    
    return -entropy

# Verify that our function matches our answer from earlier
entropy = calc_entropy([1,1,0,0,1])
print(entropy)

information_gain = entropy - ((.8 * calc_entropy([1,1,0,0])) + (.2 * calc_entropy([1])))
print(information_gain)

median = income["age"].median()
less_than_median = income[income["age"] <= median]
more_than_median = income[income["age"] > median]
'''
zeroes_less_than_median = less_than_median[less_than_median["high_income"] == 0]
prob0_less= zeroes_less_than_median.shape[0]/less_than_median.shape[0]
prob1_less= 1 - prob0_less

zeroes_more_than_median = more_than_median[more_than_median["high_income"] == 0]

prob0_more= zeroes_more_than_median.shape[0]/more_than_median.shape[0]
prob1_more= 1 - prob0_more
'''
count1 = less_than_median.shape[0]/income.shape[0]
count2 = more_than_median.shape[0]/income.shape[0]
income_entropy = calc_entropy(income["high_income"])
age_information_gain = income_entropy - ((count1 * calc_entropy (less_than_median ["high_income"] ))  + (count2 * calc_entropy (more_than_median ["high_income"] )))

print(age_information_gain)


## 12. Finding the Best Split ##

def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a data set, column to split on, and target
    """
    # Calculate the original entropy
    original_entropy = calc_entropy(data[target_name])
    
    # Find the median of the column we're splitting
    column = data[split_name]
    median = column.median()
    
    # Make two subsets of the data, based on the median
    left_split = data[column <= median]
    right_split = data[column > median]
    
    # Loop through the splits and calculate the subset entropies
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / data.shape[0]) 
        to_subtract += prob * calc_entropy(subset[target_name])
    
    # Return information gain
    return original_entropy - to_subtract

# Verify that our answer is the same as on the last screen
print(calc_information_gain(income, "age", "high_income"))

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

information_gains = []
for column in columns:
    information_gains.append(calc_information_gain(income, column, "high_income"))

index_max = information_gains.index(max(information_gains))
highest_gain = columns[index_max]