def CubeRoot(c):
    print("c = %d" % c)
    g = c / 2
    cnt = 0
    while (abs(g * g * g - c) > 0.00000000001):
        g = (2 * g + c / (g * g)) / 3
        cnt +=1
        print ("%d:%.13f"%(cnt,g))

CubeRoot(10)