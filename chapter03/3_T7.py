def GCD(m,n):
    if m < n:
        m, n = n, m
    while n != 0:
        r = m % n
        m, n = n, r
    return m

m, n= int(input("请输入整数m：")), int(input("请输入整数n："))

print("最大公约数为：", GCD(m,n))