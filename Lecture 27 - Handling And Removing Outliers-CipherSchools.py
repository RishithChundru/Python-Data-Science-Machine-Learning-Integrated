import pandas as pd

# Load the dataset
data={
    'Name': ['Alice','Bob','Charlie','David','Eve','Frank','Grace','Hank','Ivy','Jack'],
    'Age': [25,30,35,50,28,40,50,60,32,45],
    'Salary': [50000,1200000,70000,60000,80000,55000,85000,90000,1500000,62000],
    'Department': ['HR','Engineering','Engineering','HR','HR','Sales','Sales','Sales','Engineering','Engineering']
}
df=pd.DataFrame(data)
print(df)


# Visualizing Outliers using Boxplots
import matplotlib.pyplot as plt

# Box Plot to visualize outliers in the age column
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.boxplot(df['Age'].dropna())
plt.title('Boxplt of Age')

# BoxPlot to visualize outliers in the Salary column
plt.subplot(1, 2, 2)
plt.boxplot(df['Salary'].dropna())
plt.title('BoxPlot of Salary')
plt.show()


# Handling Outliers - Capping Outliers

# Capping the outliers using IQR method
df_capped=df.copy()
for column in ['Age','Salary']:
    Q1=df_capped[column].quantile(0.25)
    Q3=df_capped[column].quantile(0.75)
    IQR=Q3-Q1
    lower_bound=Q1-1.5*IQR
    upper_bound=Q3+1.5*IQR
    df_capped[column]=df_capped[column].apply(lambda x: upper_bound if x > upper_bound else (lower_bound if x < lower_bound else x))
print('Data after capping outliers using IQR method')
print(df_capped)


# Replacing Outliers with Mean/Median
df_replaced=df.copy()
for column in ['Age','Salary']:
    Q1=df_capped[column].quantile(0.25)
    Q3=df_capped[column].quantile(0.75)
    IQR=Q3-Q1
    lower_bound=Q1-1.5*IQR
    upper_bound=Q3+1.5*IQR
    median=df_replaced[column].median()
    df_replaced[column]=df_replaced[column].apply(lambda x: median if x > upper_bound  or x < lower_bound else x)
print('Data after replacing outliers using median values:')
print(df_replaced)