import matplotlib.pyplot as plt
import numpy as np
def f(x, y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
x, y = np.meshgrid(x,y)

plt.contourf(x,y,f(x,y),8,alpha = .75, cmap = 'jet')
c = plt.contour(x,y,f(x,y), 8, colors= 'black', linewidth = .5)
plt.show()