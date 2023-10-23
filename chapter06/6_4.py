import numpy as np

A = np.array([[2, 1], [4, 5]])
X = np.array([[1],[1]])

def getEv(A, v):
    Av = np.array(np.dot(A, v))
    return np.vdot(Av,v) / np.vdot(v,v)

X = X / np.vdot(X,X)
# print(X)
ev = getEv(A, X)

while (1):
    temp = np.dot(A, X)
    temp = temp / np.vdot(temp,temp)

    newev = getEv(A, temp)
    if abs(ev - newev) <= 0.001:
        break
    X = temp
    ev = newev

print(newev)
print(X)