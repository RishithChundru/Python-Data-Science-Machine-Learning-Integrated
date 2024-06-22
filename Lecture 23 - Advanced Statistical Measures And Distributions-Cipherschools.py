# MEAN
import pandas as pd

# Sample data
data={
    'Age':[25,30,35,50,28,40,50,60,32,45],
    'Salary':[50000,1200000,70000,60000,80000,55000,85000,90000,1500000,62000]
}
df=pd.DataFrame(data)

# Mean
mean_age=df['Age'].mean()
mean_salary=df['Salary'].mean()

print("Mean age: ",mean_age)
print("Mean Salary: ",mean_salary)


# Median
median_age=df['Age'].median()
median_salary=df['Salary'].median()

print("Median age: ",median_age)
print("Median Salary: ",median_salary)


# Mode
mode_age=df['Age'].mode()[0]
mode_salary=df['Salary'].mode()[0]

print("Mode age: ",mode_age)
print("Mode Salary: ",mode_salary)


# Standard Deviation
std_age=df['Age'].std()
std_salary=df['Salary'].std()

print("Standard Deviation age: ",std_age)
print("Standard Deviation Salary: ",std_salary)


# Variance
var_age=df['Age'].var()
var_salary=df['Salary'].var()

print("Variance Age: ",var_age)
print("Variance Salary: ",var_salary)


# Normal Distribution
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Normal distribution
mu, sigma=0,0.1
s=np.random.normal(mu, sigma, 1000)

# Plotting the histogram
count, bins, ignored =plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
plt.title('Normal Distribution')
plt.show()


# Binomial Distribution
n, p=10, 0.5
binomial=np.random.binomial(n, p, 1000)

# plotting the histogram
plt.hist(binomial, bins=10, density=True, alpha=0.6, color='b')
plt.title('Binomial Distribution')
plt.show()


# Quartile
import numpy as np

# Sample Data
data=[1,2,3,4,5,6,7,8,9,10]

# Calculate Quartiles
Q1=np.percentile(data,25)
Q2=np.median(data)
Q3=np.percentile(data,75)
IQR=Q3-Q1

print(f"Q1: {Q1}")
print(f"Q2 (Median): {Q2}")
print(f"Q3: {Q3}")
print(f"IQR: {IQR}")


# Z-Scores
import numpy as np

# Sample Data
data=[1,2,3,4,5,6,7,8,9,10]

# Calculate mean and standard deviation
mean=np.mean(data)
std_dev=np.std(data)

# Calculate Z-scores
z_scores=[(x-mean)/std_dev for x in data]

print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")
print("Z-Scores:",z_scoresf)