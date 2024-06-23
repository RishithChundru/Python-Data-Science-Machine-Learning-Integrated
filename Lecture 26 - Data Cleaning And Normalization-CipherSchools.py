import pandas as pd

# Load the dataset
data={
    'Name': ['Alice','Bob','Charlie','David','Eve','Frank','Grace','Hank'],
    'Age': [25.0,30.0,35.0,None,28.0,40.0,50.0,60.0],
    'Salary': [50000.0,None,70000.0,60000.0,80000.0,55000.0,85000.0,90000.0],
    'Department': ['HR','Engineering','Engineering','HR','HR','Sales','Sales','Sales']
}
df=pd.DataFrame(data)
print(df)

# Identifying the missing value
print(df.isnull().sum())

df.info()


# Removing rows with missing values
df_cleaned=df.dropna()
print(df_cleaned)


# Filling Missing values
df_filled=df.fillna({
    'Age': df['Age'].mean(),
    'Salary':df['Salary'].mean()
})
print(df_filled)


# Forward Fill Method
df_ffill=df.fillna(method='ffill')
print(df_ffill)


# Backward Fill Method
df_bfill=df.fillna(method='bfill')
print(df_bfill)


# Removing Duplicates

# Add duplicates rows for demonstration
df=pd.concat([df, df.iloc[[0]], df.iloc[[1]]], ignore_index=True)
print('Before removing duplicates:\n',df)

# Remove duplicates rows
df_no_duplicates=df.drop_duplicates()
print('After removing duplicates:\n',df_no_duplicates)


# Replacing Incorrect Values

# Replace incorrect values in the 'Department' column
df_Corrected=df.replace({'Department': {'HR': 'Human Resources','Sales': 'Sales Department'}})
print(df_Corrected)


# Ensuring Consistency

# Convert all department names to lowercase for consistency
df['Department']=df['Department'].str.lower()
print(df)


# Min-Max Normalization

# Apply min-max normilization using the formula
df_normalized = df.copy()
for col in ['Age','Salary']:
    df_normalized[col]=(df[col] - df[col].min()) / (df[col].max() - df[col].min())
    
# print original and normalized values
print('Original Dataframe: ')
print(df)
print("\nNormalized DataFrame: ")
print(df_normalized)