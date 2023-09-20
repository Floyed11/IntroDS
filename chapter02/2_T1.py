n = (int)(input("请输入一个正整数: "))
sum = n
listAns = []
cnt3 = 0
cnt2 = 0
while (sum - 3 >= 2 or sum == 3):
    listAns.append(3)
    sum -= 3
    cnt3 += 1
while (sum >= 2):
    listAns.append(2)
    sum -= 2
    cnt2 += 1
if (sum == 1):
    listAns.append(1)
print("数列为：{}个2, {}个3".format(cnt2,cnt3))
