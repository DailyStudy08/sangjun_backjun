import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]
def front(n):
    if n != '.':
        print(n, end='')
        front(tree[n][0])
        front(tree[n][1])

def middle(n):
    if n != '.':
        middle(tree[n][0])
        print(n, end='')
        middle(tree[n][1])

def end(n):
    if n != '.':
        end(tree[n][0])
        end(tree[n][1])
        print(n, end='')

front('A')
print()
middle('A')
print()
end('A')
