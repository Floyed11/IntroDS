import re
ID = input("请输入身份证号：")
pattern = "(^\d{15}$)|(^\d{17}([0-9]|x)$)"
#pattern = "^(1[1-5]|2[1-3]|3[1-7]|4[1-6]|5[0-4]|6[1-5]|7[1-3]|8[1-2]|9[1-2])\d{4}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2]\d|3[0-1])\d{3}(\d|X|x)$"
if re.match(pattern, ID):
    print("身份证号码格式正确！")
else :
    print("身份证号码格式错误！")