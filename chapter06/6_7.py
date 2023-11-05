
def Statistic(file):
    f = open(file)
    dictionary = {}
    for line in f.readlines():
        if len(line)>10:
            mark = [',','.',':','\'',';',')','(','?','!','\"']
            for i in mark:
                line = line.replace(i,' ')
            lineattr = line.strip().split(' ')
            for word in lineattr:
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    a = sorted(dictionary.items(),key=lambda item:item[1],reverse=True)
    return a

def printWords(file,n):
    a = Statistic(file)
    for i in range(n):
        print(a[i][0],a[i][1])

printWords('./chapter06/book.py',20)
