def Sqr(c):
    print("c = %d" % c)
    g = c / 2
#    g = c
#    g = c / 4

    cnt = 0
    while (abs(g * g - c) > 0.00000000001):
        g = (g+c/g)/2
        cnt +=1
        print ("%d:%.13f"%(cnt,g))

Sqr(2)
Sqr(2000)