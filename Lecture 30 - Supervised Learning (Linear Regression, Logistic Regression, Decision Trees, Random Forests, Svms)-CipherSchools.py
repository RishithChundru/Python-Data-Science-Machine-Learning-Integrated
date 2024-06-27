# Linear Regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generating synthetic data
import numpy as np
X=np.random.rand(100,1)*10
y=2.5 * X + np.random.randn(100,1) * 2

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
model=LinearRegression()
model.fit(X_train,y_train)

# Making predictions
y_pred=model.predict(X_test)

# Evaluating the model
mse=mean_squared_error(y_test,y_pred)
print(f'Meaan Squared Error: {mse}')

print(y_pred)
print(y_test)


# Logistic Regression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Loading the Iris Dataset
iris=load_iris()
X=iris.data
y=iris.target

# Using only two classes for binary classification
X = X[y != 2]
y = y[y != 2]

# Splitting data into training and testting sets
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
model=LogisticRegression()
model.fit(X_train,y_train)

# making predictions
y_pred=model.predict(X_test)

# Evaluating the model
accuracy=accuracy_score(y_test,y_pred)
print(f'Accuracy: {accuracy}')


# Decision Tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

## Loading the Iris dataset
iris=load_iris()
X=iris.data
y=iris.target

# Splitting data into training and testting sets
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
model=DecisionTreeClassifier()
model.fit(X_train,y_train)

# making predictions
y_pred=model.predict(X_test)

# Evaluating the model
accuracy=accuracy_score(y_test,y_pred)
print(f'Accuracy: {accuracy}')


# Support Vector Machine(SVM)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# loading the Iris Dataset
iris=load_iris()
X=iris.data
y=iris.target

# Using only two classes for binary classification
X = X[y != 2]
y = y[y != 2]

# Splitting data into training and testting sets
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
model=SVC()
model.fit(X_train,y_train)

# making predictions
y_pred=model.predict(X_test)

# Evaluating the model
accuracy=accuracy_score(y_test,y_pred)
print(f'Accuracy: {accuracy}')