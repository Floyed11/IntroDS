def DtoB(n):
    n_bin = 0.0
    tem = 0
    n_use = n // 1
    while n_use > 0:
        tem = tem * 10 + n_use % 2
        n_use = n_use // 2

    n_temp = 0.0
    n_temp = n - (n // 1)
    i = 0
    while n_temp > 0:
        i = i + 1
        n_temp = n_temp * 2
        n_bin = n_bin + (n_temp // 1) / (10 ** i)
        n_temp = n_temp - (n_temp // 1)
    n_bin = n_bin + tem
    return n_bin

n = float(input("请输入一个十进制数："))
print("二进制数为：", DtoB(n))