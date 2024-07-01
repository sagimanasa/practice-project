class Node:
    def __init__(self,left = None,value = None,right = None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if self.root is None:
            self.root=Node(None,value,None)
        else:
            self.rec(self.root,value)
    def rec(self, node, value):
        if value < node.value:
            if node.left is not None:
                self.rec(node.left,value)
            else:
                node.left = Node(None,value,None)
        elif value > node.value:
            if node.right is not None:
                self.rec(node.right, value)
            else:
                node.right = Node(None,value,None)



