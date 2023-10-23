import numpy as np

X = np.array([[1, -1, 4], [2, 1, 3], [1, 3, -1]])

cov = np.cov(X)

print(cov)

# 计算协方差矩阵完成