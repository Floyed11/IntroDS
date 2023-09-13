s = input("请输入一个字符串: ")
slen = len(s)
i = 0
cnt = 1
flag = False
while i < slen:
    while i+1<slen-1 and s[i+1] == s[i]:
        cnt+=1
        i+=1
    if cnt>1:
        print("有{}个连续的{}".format(cnt,s[i]))
        flag = True
    cnt = 1
    i+=1
if (not flag):
    print("没有连续的字符")