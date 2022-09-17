from collections import deque
import copy
import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
start = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start.append((i, j))
cnt = 0
answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(y, x):
    global cnt, answer
    if cnt == 3:
        a = bfs()
        if a > answer:
            answer = a
        return
    for i in range(n):
        for j in range(m):
            if i < y and j < x:
                continue
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                dfs(i,j)
                graph[i][j] = 0
                cnt -= 1

def bfs():
    graph_b = copy.deepcopy(graph)
    safe = 0
    visit = [[0 for _ in range(m)]for _ in range(n)]
    q = deque()
    q.extend(start)
    while q:
        y, x = q.popleft()
        visit[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and visit[ny][nx] == 0 and graph_b[ny][nx] != 1:
                graph_b[ny][nx] = 2
                q.append((ny, nx))
                visit[ny][nx] = 1
    
    for i in range(n):
        for j in range(m):
            if graph_b[i][j] == 0:
                safe += 1
    return safe

dfs(0,0)
print(answer)