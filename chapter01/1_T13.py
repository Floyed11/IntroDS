try:
    n = int(input("请输入一个大于0的数: "))
except:
    print("输入错误")
ans = 1
for i in range(1, n+1):
    ans *= i
print("n的阶乘为:", ans)