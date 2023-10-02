point = int(input("请输入一个百分制的成绩："))
print("成绩等级为：", end="")
if point < 60:
    print("不及格")
elif point <= 74:
    print("合格")
elif point <= 89:
    print("良好")
else:
    print("优秀") 