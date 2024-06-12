# Creating a Data Frame from a Dictionary

import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice','Bob','Charlie'],
    'Age': [25,30,35],
    'City': ['New York','Los Angeles','Chicago']
}

df=pd.DataFrame(data)
print(df)

# Creating a Data frame from a list of Dictionaries
data = [
    {'Name': 'Alice','Age': 25,'City': 'New York'},
    {'Name': 'Bob','Age': 30,'City': 'Los Angeles'},
    {'Name': 'Charlie','Age': 35,'City': 'Chicago'}
]

df=pd.DataFrame(data)
print(df)

# Creating a Dataframe from a csv file

# Assuming 'data.csv' is csv file in the current directory
"""df=pd.read_csv('dataset.csv')
print(df)"""


# Viewing Data

# Display the first few rows
print(df.head()) # It retrieves first 5 rows

# Display the last few rows
print(df.tail())

# Getting information about dataframe
print(df.info())

# Descriptive Statistics
print(df.describe())

# Selecting a single column
print(df['Name'])

# Selecting Multiple columns
print(df[['Name','City']])

# Filtering rows based on a condition
print(df[df['Age']>30])


# Adding New Columns
df['Salary']=[50000,60000,70000]
print(df)

# Modifying Existing Columns
df['Age']=df['Age']+1
print(df)

# Dropping Columns and Rows

# Dropping a column
df=df.drop(columns=['Salary'])
print(df)

# Dropping a Row
df=df.drop(index=1)
print(df)


# Grouping Data

# Grouping data byy a column
grouped=df.groupby('City')
print(grouped['Age'].mean())


# Aggregating data
aggregated=df.groupby('City').agg({'Age':['mean','min','max']})
print(aggregated)


# merging DataFrames
df1=pd.DataFrame({'ID':[1,2,3], 'Name': ['Alice','Bob','Charlie']})
df2=pd.DataFrame({'ID':[1,2,4], 'Salary': [50000,60000,70000]})

# Merging DataFrames on a common column
merged_df=pd.merge(df1,df2,on='ID',how='inner')
print(merged_df)
merged_df=pd.merge(df1,df2,on='ID',how='outer')
print(merged_df)

# Joining Data Frames
df1=pd.DataFrame({'Name': ['Alice','Bob'], 'Age': [25,30]},index=[0,1])
df2=pd.DataFrame({'City':['New York','Los Angeles']},index=[0,2])

# joining DataFrames on their index
joined_df=df1.join(df2,how='left')
print(joined_df)