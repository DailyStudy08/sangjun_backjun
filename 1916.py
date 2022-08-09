from collections import deque

city = int(input())
bus = int(input())
INF = 1000000
graph = [[]for _ in range(city)]
visit = [False]*city
arr = [[INF for _ in range(city)] for _ in range(city)]

for i in range(city):
    arr[i][i] = 0

for _ in range(bus):
    a, b, value = map(int,input().split())
    arr[a][b] = value
    graph[a].append(b)
    arr[b][a] = value
    graph[b].append(a)

start, end = map(int, input().split())

def bfs(start) :
    queue = deque([start])
