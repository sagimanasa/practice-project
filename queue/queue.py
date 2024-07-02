class Node:#class to create nodes of linkedlist
    def __init__(self,value=None):
        self.value = value
        print(value)
        self.address = None

class Queue:
    def __init__(self):
        self.head = Node()#head is default null
        self.tail = self.head#tail points head position

    def is_empty(self):#checking whether queue is empty or not
        if self.head.address is None:
            return True
        return False
    def insert(self,value):#method to add data to queue
        temp=Node(value)
        self.tail.address=temp
        self.tail = temp
        print(value)

    def pop(self):
        self.head=self.head.address
        return self.head.value

arr = [1,2,3,4,5,6,7]
que = Queue()
for item in arr:
    print(item)
    que.insert(item)
    print(que)


while(not que.is_empty()):
    x = que.pop()
    print(x)
