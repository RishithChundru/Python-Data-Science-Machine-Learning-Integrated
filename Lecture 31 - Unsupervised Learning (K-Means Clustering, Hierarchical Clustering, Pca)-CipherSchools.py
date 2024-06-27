# K-Means Clustering
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generating the synthetic data
X, y=make_blobs(n_samples=300, centers=4,cluster_std=0.60,random_state=0)

# Training the model
model=KMeans(n_clusters=4)
y_pred=model.fit_predict(X)

# Plotting the results
plt.scatter(X[:, 0],X[:, 1], c=y_pred,cmap='rainbow')
plt.scatter(model.cluster_centers_[:, 0],model.cluster_centers_[:, 1],s=300,c='black',marker='x')
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()


# Hierarchical Clustering
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

# Generating the synthetic data
X, y=make_blobs(n_samples=300, centers=4,cluster_std=0.60,random_state=0)

# Training the model
model=AgglomerativeClustering(n_clusters=4)
y_pred=model.fit_predict(X)

# Plotting the results
plt.scatter(X[:, 0],X[:, 1], c=y_pred,cmap='rainbow')
plt.title('Hierarchical Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()


# Principal Component Analysis(PCA)
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Loading the iris dataset
iris=load_iris()
X=iris.data
y=iris.target

# Applying PCA
pca=PCA(n_components=2)
X_pca=pca.fit_transform(X)

#Plotting the results
plt.scatter(X_pca[:, 0],X[:, 1], c=y,cmap='rainbow')
plt.title('PCA on Iris dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()