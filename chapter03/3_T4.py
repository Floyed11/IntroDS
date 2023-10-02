class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = None
        self.lenth = 0

    def insert(self, pos, value):
        if pos < 0 or pos > self.lenth:
            raise IndexError("Index out of range!")
        node = Node(value)
        if pos == 0:
            node.next = self.head.next
            self.head.next = node
        else:
            p = self.head.next
            while pos > 1:
                p = p.next
                pos -= 1
            node.next = p.next
            p.next = node
        self.lenth += 1
    
    def delete(self, pos):
        if pos < 0 or pos >= self.lenth:
            raise IndexError("Index out of range!")
        if pos == 0:
            self.head.next = None
        else:
            temp = self.head.next
            while pos > 1:
                temp = temp.next
                pos -= 1
            temp.next = temp.next.next
        self.lenth -= 1

    def update(self, pos, value):
        if pos < 0 or pos >= self.lenth:
            raise IndexError("Index out of range!")      
        temp = self.head.next
        while pos > 0:
            temp = temp.next
            pos -= 1
        temp.data = value

    def search(self, value):
        temp = self.head.next
        pos = 0
        while temp:
            if temp.data == value:
                return pos
            temp = temp.next
        return -1
    
    def print(self):
        temp = self.head.next
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()
    
linklist = LinkedList    
linklist.__init__(linklist) 
while True:
    s = input().split(' ')
    opt = s[0]
    if opt == 'i':
        p = int(s[1])
        x = int(s[2])
        linklist.insert(linklist, p, x)
        linklist.print(linklist)
    elif opt == 'd':
        x = int(s[1])
        linklist.delete(linklist, x)
        linklist.print(linklist)
    elif opt == 's':
        x = int(s[1])
        print(linklist.search(linklist, x))
    elif opt == 'u':
        p = int(s[1])
        x = int(s[2])
        linklist.update(linklist, p, x)
        linklist.print(linklist)
    