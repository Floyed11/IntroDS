import math
num = int(input(""))

def is_Prime(n):
    flag = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            flag = False
            break
    return flag

if is_Prime(num):
    print("yes")
else:
    print("no")