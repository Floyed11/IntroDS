import numpy as np

A = np.array([[2,1],[4,5]])

eva, evt = np.linalg.eigh(A)
print("特征值为：", eva)
print("特征向量为：", evt)