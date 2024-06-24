# Handling Missing Values

import pandas as pd
from sklearn.impute import SimpleImputer

# Sample Data
data={
    'Feature 1': [1.0, 2.0, None, 4.0, 5.0],
    'Feature 2': [2.0, None, 4.0, 5.0, None],
    'Feature 3': [None, 3.0, 3.5 , 4.0, 4.5]
}
df=pd.DataFrame(data)

# handling Missing Values
imputer=SimpleImputer(strategy='mean')
df_imputed=pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print("After Imputation:\n",df_imputed)


# Encoding Categorical values
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample data
data={
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']
}
df=pd.DataFrame(data)

# Encoding categorical variables
encoder=OneHotEncoder(sparse_output=False)
encoded_categories=encoder.fit_transform(df[['Color']])
df_encoded=pd.DataFrame(encoded_categories, columns=encoder.get_feature_names_out(['Color']))
df=pd.concat([df, df_encoded], axis=1).drop('Color', axis=1)
print("After One-Hot Encoding:\n", df)


# Feature Scaling
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Sample Data
data={
    'Feature 1': [10,20,30,40,50],
    'Feature 2': [100,200,300,400,500]
}
df=pd.DataFrame(data)

# Feature Scaling
scaler=MinMaxScaler()
df_scaled=pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print("After Min-Max Scaling:\n",df_scaled)


# Feature Creation
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

# Sample data
data={
    'Feature 1':[1,2,3,4,5],
    'Feature 2':[2,3,4,5,6]
}
df=pd.DataFrame(data)

# feature creation
poly=PolynomialFeatures(degree=2,include_bias=False)
poly_features=poly.fit_transform(df)
df_poly=pd.DataFrame(poly_features, columns=poly.get_feature_names_out(['Feature 1','Feature 2']))
print("After creating polynomial features:\n",df_poly)


# Variance Thresholding
import pandas as pd
from sklearn.feature_selection import VarianceThreshold

# Sample data
data={
    'Feature 1': [1,1,1,1,1], # low variance
    'Feature 2': [2,3,4,5,6],
    'Feature 3': [3,4,5,6,7],
    'Feature 4': [1,1,1,1,1] # Zero variance
}
df=pd.DataFrame(data)

# variance Thresholding
selector=VarianceThreshold(threshold=0.1)
df_variance_filtered=pd.DataFrame(selector.fit_transform(df), columns=df.columns[selector.get_support()])
print("After Variance thresholding:\n",df_variance_filtered)


# Correlation Matrix Filtering
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data={
    'Feature 1': [1,2,3,4,5],
    'Feature 2': [2,4,6,8,10], # highly correlated with feature 1
    'Feature 3': [2,4,6,8,10], # highly correlated with feature 2
    'Feature 4': [5,6,7,8,9]
}
df=pd.DataFrame(data)

# Correlation matrix
corr_matrix=df.corr().abs()

# plot correlation matrix
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm',fmt='.2f')
plt.show()

# select upper triangle of correlation matrix
upper=corr_matrix.where(np.triu(np.ones(corr_matrix.shape),k=1).astype(bool))

# Find features with correlation greater than 0.9
to_drop=[column for column in upper.columns if any(upper[column]>0.9)]

# drop features 
df_corr_filtered=df.drop(to_drop, axis=1)
print("After correlation matrix filtering:\n",df_corr_filtered)



# Domain Knowledge
import pandas as pd

# sample data
data={
    'Age':[25,30,35,40,45],
    'Salary':[50000,60000,70000,80000,90000],
    'Height':[5.5,6.0,5.8,5.9,6.1],
    'Weight':[150,160,170,180,190]
}
df=pd.DataFrame(data)

# base on domain knowledge, we know age and salary are important
selected_features_domain=df[['Age', 'Salary']]
print("Selected Features based on Domain Knowledge:\n",selected_features_domain)
