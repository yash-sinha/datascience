## 1. Introduction to the Data ##

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv("admissions.csv")
model = LogisticRegression()
model.fit(admissions[["gpa"]], admissions["admit"])
labels = model.predict(admissions[["gpa"]])
admissions["predicted_label"] = labels
print(admissions["predicted_label"].value_counts())
print(admissions.head(5))

## 2. Accuracy ##

admissions.rename(columns = {'admit':'actual_label'}, inplace = True)
matches = admissions["actual_label"] == admissions["predicted_label"]
matches.head(5)
correct_predictions = matches[matches == True]
correct_predictions.head(5)
accuracy = len(correct_predictions)/len(matches)
print(accuracy)

## 4. Binary classification outcomes ##

true_positives = len(admissions[(admissions["actual_label"]==1) & (admissions["predicted_label"] == 1)])

true_negatives = len(admissions[(admissions["actual_label"]==0) & (admissions["predicted_label"] == 0)])

print(true_positives)
print(true_negatives)
                                
                                

## 5. Sensitivity ##

true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])

false_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)

false_negatives = len(admissions[false_negative_filter])
sensitivity = true_positives/(true_positives+ false_negatives)

## 6. Specificity ##

true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])
false_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_negative_filter])

true_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 0)
true_negatives = len(admissions[true_negative_filter])
false_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 0)
false_positives = len(admissions[false_positive_filter])
specificity = true_negatives/(true_negatives+false_positives)
