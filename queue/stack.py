class Node: #cls to create nodes of linked list
    def __init__(self,value=None,address=None):
        self.value=value
        self.address=address
class Stack:
    def __init__(self):
        self.head=Node() #head is default null

    def is_empty(self): #checks if stack is empty or not
        if self.head.address is None:
            return True
        return False

    def push(self,value): #method to add data to stack
        temp=Node(value,self.head)
        self.head=temp
    def pop(self): #remove element which is in head
        x=self.head.value
        self.head=self.head.address
        return x


arr=[1,2,3,4,5,6,7]
st=Stack()
for item in arr:#iteration of arr
    st.push(item)
    #print(st)
while(not st.is_empty()):#deleting element when stack is not empty
    y=st.pop()
    print(y)


