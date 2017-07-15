## 2. Array Comparisons ##

countries_canada = (world_alcohol[:,2]) == "Canada"
years_1984 = (world_alcohol[:,0]) == "1984"

## 3. Selecting Elements ##

country_is_algeria = (world_alcohol[:,2]) == "Algeria"
country_algeria = world_alcohol[country_is_algeria, :]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = ((world_alcohol[:,0]) == "1986") & ((world_alcohol[:,2]) == "Algeria")

rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986, :]

## 5. Replacing Values ##

is_1986 = (world_alcohol[:,0]) == "1986"
world_alcohol[is_1986,0] = "2014"

is_wine = (world_alcohol[:,3]) == "Wine"
world_alcohol[is_wine, 3] = "Grog"

## 6. Replacing Empty Strings ##

is_value_empty = (world_alcohol[:,4]=="")
world_alcohol[is_value_empty, 4] = "0"

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

canada_1986 = world_alcohol[(world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Canada"),:]

canada_1986[:, (world_alcohol[:,4] == "")] = "0"
canada_alcohol = canada_1986[:,4].astype(float)
total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating Consumption for Each Country ##

totals = {}
year = world_alcohol[world_alcohol[:,0] == "1989",:]
for c in countries:
    country_consumption = year[year[:,2]==c,:]
    country_consumption[(country_consumption[:,4]==""),4] = "0"
    con = country_consumption[:,4].astype(float)
    totals[c] = con.sum()

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for key in totals:
    if highest_value < totals[key]:
        highest_value = totals[key]
        highest_key = key