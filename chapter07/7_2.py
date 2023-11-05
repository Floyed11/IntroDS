from sklearn import datasets
import numpy as np

dataset = datasets.load_iris()
X = dataset.data
y = dataset.target

centerpoints = [[0, 0], [0, 0], [0, 0]]
count = [0] * 3

for i in range(150):
    type = y[i]
    count[type] += 1
    centerpoints[type][0] += X[i][0]
    centerpoints[type][1] += X[i][1]

for i in range(3):
    centerpoints[i][0] /= count[i]
    centerpoints[i][1] /= count[i]

print("不同标签类别数据的中心点坐标依次为：")
print(centerpoints)

for i in range(150):
    type = y[i]
    dis = (X[i][0] - centerpoints[type][0]) ** 2 + (X[i][1] - centerpoints[type][1]) ** 2
    dis = np.sqrt(dis)
    print(f"第{i+1}个数据点到中心点的距离为：{dis:.2f}")