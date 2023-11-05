from sklearn.datasets import load_iris
import sklearn
import matplotlib.pyplot as plt

iris = load_iris()

X = iris.data
y = iris.target

# 绘制散点图
plt.scatter(X[y==0, 0], X[y==0, 1], color='red', label=iris.target_names[0])
plt.scatter(X[y==1, 0], X[y==1, 1], color='blue', label=iris.target_names[1])
plt.scatter(X[y==2, 0], X[y==2, 1], color='green', label=iris.target_names[2])

# 添加图例和标题
plt.legend()
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('Iris Dataset Visualization')

# 显示图像
plt.show()