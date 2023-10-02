A = input("请输入数组A：").split()

def make(n):
    global A
    b = 1
    for i in range(len(A)):
        if (i != n):
            b = b * int(A[i])
    return b

B = []
for i in range(len(A)):
    B.append(make(i))
print(B)