import random
import math


def make_1():
    cnt = 0
    inCircle = 0
    times = 10000000
    for i in range(times):
        cnt += 1
        x = random.random()
        y = random.random()
        if (x * x + y*y)**0.5 <= 1:
            inCircle += 1
    ans = 4 * (inCircle / times)
    print("蒙特卡罗法：%.10f" % ans)
    print("次数：%d" % cnt)

def make_2():
    cnt = 1
    n = 3
    lbound = (n / 2) * math.sin(2 * math.pi / n)
    rbound = 2 * n * math.sin(math.pi / n) - n / 2 * math.sin(2 * math.pi / n)
    while ((rbound - lbound) > 0.0000000001):
        lbound = n / 2 * math.sin(2 * math.pi / n)
        rbound = 2 * n * math.sin(math.pi / n) - ((n / 2) * math.sin(2 * math.pi / n))
        cnt += 1
        n *= 2
        #print(lbound,rbound)
    ans = lbound
    print("割圆法：%.10f" % ans)
    print("次数：%d" % cnt)


def make_3():
    cnt = 0
    ans = 0
    n = 0
    while True:
        cnt += 1
        ans += (4 / (8 * n + 1) - 2 /(8 * n + 4) - 1 /(8 * n + 5)-1 /(8 * n + 6))/pow(16, n)
        if abs(ans - math.pi) < 0.0000000001:
            break
        n += 1
    print("BBP公式: %.10f" % ans)
    print("次数：%d" % cnt)


make_1()
make_2()
make_3()
