import numpy as np
import numpy.matlib

listPath = []
color = [0] * 10

def DFS(n):
    global listPath
    if n == 9:
        print(listPath)
        return
    
    color[n] = 1
    if len(listPath) > 10:
        return
    for j in range(10):
        if (ori[n,j] == 1 and color[j] == 0):
            listPath.append(j)
            color[j] = 1
            DFS(j)
            listPath.pop()
            color[j] = 0
    color[n] = 2
    return

ori = np.matlib.zeros((10, 10))
ori[0, 5] = 1
ori[1, 5] = 1
ori[1, 6] = 1
ori[1, 7] = 1
ori[2, 6] = 1
ori[2, 8] = 1
ori[3, 7] = 1
ori[3, 8] = 1
ori[4, 8] = 1
ori[4, 9] = 1
ori[5, 0] = 1
ori[5, 1] = 1
ori[6, 1] = 1
ori[6, 2] = 1
ori[7, 1] = 1
#ori[7, 2] = 1
ori[7, 3] = 1
ori[8, 2] = 1
ori[8, 3] = 1
ori[8, 4] = 1
ori[9, 4] = 1
#print(ori)

con = np.matlib.zeros((10, 1))
con[0][0] = 1
#print(con)

DFS(0)

# cnt = 0
# while cnt <= 10:
#     con = ori * con
#     cnt += 1
#     if(con[9,0] >= 1):
#         print(con)
