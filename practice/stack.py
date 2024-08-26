class Node:
    def __init__(self,value=None,address=None):
        self.value=value
        self.address=address
class Stack:
    def __init__(self):
        self.head=Node()

    def is_empty(self):
        if self.head.address is None:
            return True
        return False

    def push(self,value):
        temp=Node(value,self.head)
        self.head=temp
    def pop(self):
        x=self.head.value
        self.head=self.head.address
        return x


arr=[1,2,3,4,5]
s=Stack()
for item in arr:
    s.push(item)
while(not s.is_empty()):
    y=s.pop()
    print(y)

