from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

iris = datasets.load_iris()
X = iris.data  

kmeans = KMeans(n_clusters=3) 
kmeans.fit(X)

y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis')

plt.scatter(centers[:, 0], centers[:, 1], c='r', marker='*', s=120, alpha=0.6)

plt.title("Iris Dataset K-means Clustering")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

plt.show()