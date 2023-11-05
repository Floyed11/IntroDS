import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
# from sklearn.datasets import load_boston
from sklearn.datasets import fetch_california_housing

boston = fetch_california_housing()
# print(boston.keys())
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(boston['data'], boston['target'], test_size=0.3, random_state=2)
lr = LinearRegression()
lr.fit(X_train, y_train)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None)
''', normalize=False'''

print('训练集准确度：', lr.score(X_train, y_train))
print('测试集准确度：', lr.score(X_test, y_test))