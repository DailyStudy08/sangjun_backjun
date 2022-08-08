import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

n = int(input())
graph = [[]for _ in range(n+1)]
visit = [False]*(n+1)
for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def tree():
    queue = deque([1])
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visit[i] == False:
                queue.append(i)
                visit[i] = a

tree()
for i in visit[2:]:
    print(i)