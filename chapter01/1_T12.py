import math
num = float(input("请输入一个数字: "))
# negFlag = False
# if num<0:
#     negFlag = True

lbound = 0
rbound = max(abs(num),1)
if (num<0):
    rbound = -1 * rbound
ans = (lbound+rbound)/2
while (abs(pow(ans, 3) - num) > 0.00001):
    ansPow = (pow(ans, 3))
    if ansPow > num:
        rbound = ans
        ans = (lbound+ans)/2
    else:
        lbound = ans
        ans = (ans + rbound)/2
print("该数的三次方根为: %.3f" % ans)
