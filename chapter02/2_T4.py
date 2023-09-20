step = 0.00001
bias = 0.0001
c= 2
g = 0
for i in range(c):
    if (i * i > c and (i-1) * (i-1) <=c ):
        g = i - 1
        break

while(abs(g * g - c) > bias):
    g+=step

print('%.5f' % g)