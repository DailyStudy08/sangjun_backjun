import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque


def bfs(a, b):
    queue = deque()
    queue.append([a, 0])
    while queue:
        q, t = queue.popleft()
        for i in graph[q]:
            if i == b:
                return t+1
            if visit[i] != True:
                queue.append((i, t+1))
                visit[i] = True
    return -1

n = int(input())
a, b = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
k = int(input())
for i in range(k):
    l, m = map(int, input().split())
    graph[l].append(m)
    graph[m].append(l)
print(bfs(a, b))