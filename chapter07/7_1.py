from sklearn import datasets
from sklearn.model_selection import train_test_split

dataset = datasets.load_iris()
X = dataset.data
y = dataset.target

'''分离测试集和训练集'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

'''标准化数据'''
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

'''Logistic回归'''
clf = LogisticRegression(max_iter=1000) 

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")
