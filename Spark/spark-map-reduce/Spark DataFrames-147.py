## 1. The Spark DataFrame: An Introduction ##

with open("census_2010.json") as f:
    for i in range(0,4):
        print(f.readline())

## 2. Reading in Data ##

# Import SQLContext
from pyspark.sql import SQLContext

# Pass in the SparkContext object `sc`
sqlCtx = SQLContext(sc)

# Read JSON data into a DataFrame object `df`
df = sqlCtx.read.json("census_2010.json")

# Print the type
print(type(df))

## 3. Schema ##

sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.printSchema()

## 4. Pandas vs Spark DataFrames ##

df.show(5)

## 5. Row Objects ##

first_five = df.head(5)
for row in first_five:
    print(row.age)

## 6. Selecting Columns ##

df[['age']].show()
df.select('age', 'males', 'females').show()

## 7. Filtering Rows ##

five_plus = df[df['age'] >5]
five_plus.show()

## 8. Using Column Comparisons as Filters ##

males_more = df[df['males'] > df['females']]
males_more.show()
                                

## 9. Converting Spark DataFrames to pandas DataFrames ##

pandas_df = df.toPandas()
plt.hist(pandas_df['total'])