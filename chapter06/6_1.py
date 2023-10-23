import numpy
import math
import matplotlib.pyplot as plt

num = 100
samples = numpy.random.standard_normal(num)

print(samples)

import seaborn as sns

# 绘制密度图
sns.kdeplot(samples, shade=True, color='r')
plt.title('data distribution gragh')
plt.xlabel('value')
plt.ylabel('density')

plt.show()