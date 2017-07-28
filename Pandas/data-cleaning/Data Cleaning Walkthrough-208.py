## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for val in data_files:
    name = val.split(".")[0]
    data[name] = pd.read_csv("schools/"+val)

## 5. Exploring the SAT Data ##

data["sat_results"].head(5)

## 6. Exploring the Remaining Data ##

for val in data:
    print(data[val].head(5))

## 8. Reading in the Survey Data ##

all_survey = pd.read_csv("schools/survey_all.txt", delimiter = "\t", encoding = "windows-1252")
d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter = "\t", encoding = "windows-1252")
survey = pd.concat([all_survey, d75_survey], axis = 0)
survey.head(5)

## 9. Cleaning Up the Surveys ##

survey["DBN"] = survey["dbn"]
cols = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
survey = survey.loc[:, cols]
data["survey"] = survey

## 11. Inserting DBN Fields ##

def pad_csd(val):
    str_val = str(val)
    if len(str_val) > 1:
        return str_val
    return str_val.zfill(2)

data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]
print(data["class_size"].head())

        
    

## 12. Combining the SAT Scores ##

data["sat_results"]["SAT Math Avg. Score"] = pd.to_numeric(data["sat_results"]["SAT Math Avg. Score"], errors="coerce")

data["sat_results"]["SAT Critical Reading Avg. Score"] = pd.to_numeric(data["sat_results"]["SAT Critical Reading Avg. Score"],errors="coerce")

data["sat_results"]["SAT Writing Avg. Score"] = pd.to_numeric(data["sat_results"]["SAT Writing Avg. Score"],errors="coerce")

data["sat_results"]["sat_score"] = data["sat_results"]["SAT Math Avg. Score"] + data["sat_results"]["SAT Critical Reading Avg. Score"] + data["sat_results"]["SAT Writing Avg. Score"]

print(data["sat_results"]["sat_score"].head())

## 13. Parsing Geographic Coordinates for Schools ##

import re
def lat(inp):
    coord = re.findall("\(.+\)", inp)
    
    latlong = coord[0].replace("(","")
    return latlong.split(",")[0]

data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(lat)
print(data["hs_directory"].head())

## 14. Extracting the Longitude ##

import re
def lon(inp):
    coord = re.findall("\(.+\)", inp)
    latlong = coord[0].replace(")","")
    return latlong.split(",")[1]

data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(lon)
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"], errors = "coerce")
data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors = "coerce")
print(data["hs_directory"].head())