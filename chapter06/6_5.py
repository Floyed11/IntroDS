import numpy as np

X = np.array([[1, -1, 4], [2, 1, 3], [1, 3, -1]])

cov = np.cov(X)

print(cov)

# 计算协方差矩阵完成

A = cov

def getEv(A, v):
    Av = np.array(np.dot(A, v))
    return np.vdot(Av, v) / np.vdot(v, v)


i = 0
while i < 3:
    if i == 0:
        X = np.array([[1], [1], [1]])
    else:
        X = X / 100000
        print(X)

    X = X / np.vdot(X, X)
    # print(X)
    ev = getEv(A, X)

    while (1):
        temp = np.dot(A, X)
        temp = temp / np.vdot(temp, temp)

        newev = getEv(A, temp)
        if abs(ev - newev) <= 0.001:
            i += 1
            break
        X = temp
        ev = newev

    print(newev)
