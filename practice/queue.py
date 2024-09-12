class Node:
    def __init__(self,value=None):
        self.value=value
        self.address=None
class Queue:
    def __init__(self):
        self.head=Node()
        self.tail=self.head
    def is_empty(self):
        if self.head.address is None:
            return True
        return False
    def push(self,value):
        temp=Node(value)
        self.tail.address=temp
        self.tail=temp
    def pop(self):
        self.head=self.head.address
        return self.head.value
arr=[1,2,3,4,5]
q=Queue()
for i in arr:
    q.push(i)
while(not q.is_empty()):
    x=q.pop()
    print(x)


