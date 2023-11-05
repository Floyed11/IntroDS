from sklearn import datasets
import torch

dataset = datasets.load_iris()
data = dataset['data']
iris_type = dataset['target']

input = torch.FloatTensor(dataset['data'])
# print(input)
label = torch.LongTensor(dataset['target'])
# print(label)

import torch.nn.functional as Fun
# 定义BP神经网络
class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.out = torch.nn.Linear(n_hidden, n_output)
        
    def forward(self,x):
        x = Fun.relu(self.hidden(x))
        x = self.out(x)
        return x
    
net = Net(n_feature=4, n_hidden=10, n_output=3)
optimizer = torch.optim.SGD(net.parameters(), lr=0.05)
# SGD:随机梯度下降法
loss_func = torch.nn.CrossEntropyLoss()
# 设定损失函数

for i in range(1000):
    out = net(input)
    loss = loss_func(out, label)
    # 输出与label对比
    optimizer.zero_grad()
    # 初始化
    loss.backward()
    optimizer.step()

out = net(input)
# out是一个计算矩阵
prediction = torch.max(out, 1)[1]
pred_y = prediction.numpy()
# 预测y输出数列
target_y = label.data.numpy()
# 实际y输出数据

accuracy = sum(pred_y == target_y) / len(target_y)
print("预测准确度为：", accuracy)