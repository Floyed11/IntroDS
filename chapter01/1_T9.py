print("请输入一个序列，用逗号隔开")
list1 = input().split(',')

#for 方法
list2 = []
for i in list1[::-1]:
    #print(i,end=' ')
    list2.append(i)
print("for方法")
print(list2)
print()

#while 方法
cnt = 0
l = len(list1) - 1
while cnt<(l//2):
    list1[cnt],list1[l - cnt] = list1[l - cnt],list1[cnt]
    cnt+=1
print("while方法")
print(list1)