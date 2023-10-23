import numpy as np

A = np.array([[1, -1, 4], [2, 1, 3], [1, 3, -1]])

A = np.cov(A)

def getEv(A, v):
    Av = np.array(np.dot(A, v))
    return np.vdot(Av, v) / np.vdot(v, v)


i = 0
while i < 3:
    X = np.array([[1], [1], [1]])
    X = X / np.vdot(X, X)
    ev = getEv(A, X)

    while (1):
        temp = np.dot(A, X)
        temp = temp / np.linalg.norm(temp)
        newev = getEv(A, temp)
        X = temp
        ev = newev
        if ev / newev <= 1.001 and ev / newev >= 0.999:
            i += 1
            A = A - newev * np.dot(X, X.T)
            break

    print(ev)