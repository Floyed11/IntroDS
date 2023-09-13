try:
    x = int(input("请输入 x="))
    y = int(input("请输入 y="))
    z = int(input("请输入 z="))
except:
    print("请输入数字")

#list1 = [x,y,z]
#print(isinstance(x,int),type(x),x.isdigit())
#print(((x.isdigit()) and (y.isdigit()) and (z.isdigit())))
# while (not((x.isdigit()) and (y.isdigit()) and (z.isdigit()))):
#     print("请输入数字")
#     x = input("请输入 x=")
#     y = input("请输入 y=")
#     z = input("请输入 z=")
#     list1 = [x,y,z]
# list1.sort()
# print("从小到大依次为：")
# for i in list1:
#     print(i,sep=' ')
if (x > y):
    x,y = y,x
if (y > z):
    y,z = z,y
if (x > y):
    x,y = y,x
print("从小到大依次为：")
print(x,y,z,sep=' ')