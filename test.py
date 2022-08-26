import sys
<<<<<<< HEAD
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
=======
sys.stdin = open('input.txt', 'r')

def check(arr):
    global ans
    # 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
                if cnt >= 5:
                    ans = 'YES'
                    return
            else:
                cnt = 0
    
    # 세로
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 'o':
                cnt += 1
                if cnt >= 5:
                    ans = 'YES'
                    return
            else:
                cnt = 0

    # 대각석 우측방향
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            y, x = i, j
            cnt = 0
            while 0 <= y < N and 0 <= x < N and arr[y][x] == 'o' and visited[y][x] == 0:
                visited[y][x] = 1
                cnt += 1
                if cnt >= 5:
                    ans = 'YES'
                    return
                y += 1
                x += 1

    # 대각선 좌축 방향
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            y, x = i, j
            cnt = 0
            while 0 <= y < N and 0 <= x < N and arr[y][x] == 'o' and visited[y][x] == 0:
                visited[y][x] = 1
                cnt += 1
                if cnt >= 5:
                    ans = 'YES'
                    return
                y += 1
                x -= 1



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 'NO'
    check(arr)
    print(f'#{tc} {ans}')
>>>>>>> b48f02a9dd815ad2864fa184797568dc92dd7add
