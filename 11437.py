import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

n = int(input())

parents = [i for i in range(n+1)]
depth = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    visit = [0 for _ in range(n+1)] 
    q = deque()
    q.append((1, 0))
    visit[1] = 1
    while q:
        node, deep = q.pop()
        for i in graph[node]:
            if visit[i] == 0:
                visit[i] = 1
                depth[i] = deep + 1
                parents[i] = node
                q.append((i, deep + 1))
                
def ancester(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    while depth[a] != depth[b]:
        b = parents[b]
    while a != b:
        a = parents[a]
        b = parents[b]
    return a

bfs()
m = int(input())
cache = dict()
for _ in range(m):
    a, b = map(int, input().split())
    if (a, b) in cache:
        print(cache[(a, b)])
    else:
        cache[(a, b)] = cache[(b, a)] = ancester(a, b)
        print(cache[(a, b)])