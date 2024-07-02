class Node:  # creating node class
    def __init__(self, left = None, value = None, right = None):
        self.value = value
        self.left = left
        self.right = right


class Tree:#creating tree class
    def __init__(self):
        self.root = None
    def insert(self, value):#if there is no value in root value will be placed
        if self.root is None:
            self.root = Node(None, value, None)
        else:
            self.rec(self.root, value)
    def rec(self, node, value):
        if value < node.value: #node.value==root
            if node.left is not None: # if value is less than root node it will be placed in left side of the root node
                self.rec(node.left, value)
            else:
                node.left = Node(None, value, None)
        elif value > node.value:# if value is greater than root node the value is placed in right side of root node
            if node.right is not None:
                self.rec(node.right, value)
            else:
                node.right = Node(None, value, None)

    def displayrec(self, node):
        if node.left is not None:
            self.displayrec(node.left)
        print(node.value)
        if node.right is not None:
            self.displayrec(node.right)

    def display(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.displayrec(self.root)

    def getrec(self, node, arr):
        if node.left is not None:
           self.getrec(node.left, arr)
        arr.append(node.value)
        if node.right is not None:
            self.getrec(node.right, arr)


    def get(self):
        output=[]
        if self.root is None:
            print("empty tree")
        else:
            self.getrec(self.root, output)

        return output

arr = [2,6,1,9,4,5]
tree = Tree()
#tree.display()
for value in arr:
    tree.insert(value)
    tree.display()
    print("#########################################")
    print(tree.get())
tree.display()
print("#######")
print(tree.get())
