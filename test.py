import sys
sys.stdin = open('input.txt')
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    

class MyTree:
    def __init__(self, data):
        self.root = Node(data)

    def add_node(self, parent, child):
        p_node = self.get_node(self.root, parent)
        if p_node.left == None:
            p_node.left = Node(child)
        else:
            p_node.right = Node(child)

    def get_node(self, current, val):
        if current == None:
            return None
        if current.data == val:
            return current
        result1 = self.get_node(current.left, val)
        result2 = self.get_node(current.right, val)
        if result1 != None:
            return result1
        if result2 != None:
            return result2
        return None

    def print_nodes(self):
        self.preorder(self.root)

    def preorder(self, node):
        if node == None:
            return
        print(node.data, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)
        

    def inorder(self, node):
        if node == None:
            return
        self.preorder(node.left)
        print(node.data, end=' ')
        self.preorder(node.right)

    def postorder(self, node):
        if node == None:
            return
        self.preorder(node.left)
        self.preorder(node.right)
        print(node.data, end=' ')

V = int(input())
data = list(map(int, input().split()))
tree = MyTree(1)
for i in range(V-1):
    data[i*2], data[i*2+1]
    tree.add_node(data[i*2], data[i*2+1])
tree.print_nodes()