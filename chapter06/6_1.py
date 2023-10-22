import numpy
import math
import matplotlib.pyplot as plt

num = 100
samples = numpy.random.standard_normal(num)

# print(samples)

# index = 0.1
# cnt = {}
# xlist = []
# i = -400
# while i <= 400:
#     cnt[i] = 0
#     xlist.append(i)
#     i += 1

# for i in samples:
#     cnt[int(i*100)] += 1

# plt.plot(xlist, cnt.values())

# plt.scatter(samples, numpy.zeros(num), marker='o', color='r')

import seaborn as sns

# 绘制密度图
sns.kdeplot(samples, shade=True, color='r')
plt.title('data distribution gragh')
plt.xlabel('value')
plt.ylabel('density')

plt.show()