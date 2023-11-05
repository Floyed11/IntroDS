from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from torch_geometric.datasets import Planetoid

dataset = Planetoid(root='/Users/linto/Documents/IntroDaSE/Homework/IntroDS/chapter08/', name='cora')
data = dataset[0]

X = data.x.numpy()
y = data.y.numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=16)

clf = MultinomialNB()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print('Accuracy:', accuracy)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)

# 训练kNN分类器
knn.fit(X_train, y_train)

accuracy = knn.score(X_test, y_test)
print('Accuracy2:', accuracy)

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

pca = PCA(n_components=2)
# 对分类结果进行降维处理
X_pred = knn.predict(X_train)
X_pred = X_pred.reshape(-1, 1)
X_pd = np.concatenate((X_train, X_pred), axis=1)

X_train_pca = pca.fit_transform(X_pd)

# 使用matplotlib库的scatter函数进行二维展示
plt.figure(figsize=(8, 6))
plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=y_train, cmap='rainbow')
plt.show()