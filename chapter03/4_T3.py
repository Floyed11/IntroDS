import random

list1 = [random.randint(0, 100) for i in range(10)]
#list2 = [random.randint(0, 100) for i in range(100)]

print("before: ", list1)
def insert_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp
    return list

print("after: ", insert_sort(list1))
