import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Generate sample data
data={
    'Age': np.random.normal(30, 10, 100).astype(int),
    'Annual Income (K$)': np.random.normal(50, 20, 100).astype(int),
    'Spending Score (1-100)': np.random.randint(1, 100, 100),
    'Years with Company': np.random.normal(5, 2, 100).astype(int)
}

# Creating DataFrame
df=pd.DataFrame(data)
print(df)


# Tabulate
from tabulate import tabulate

correlation_matrix=df.corr()

# Print the correlation matrix as a table
print(tabulate(correlation_matrix,headers='keys',tablefmt='grid',numalign="right",floatfmt=".2f"))
