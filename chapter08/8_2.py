from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

y_accuracy = knn.score(X_test, y_test)
X_accuracy = knn.score(X_train, y_train)
print('test_accuracy: ', y_accuracy)
print('train_accuracy: ', X_accuracy)

