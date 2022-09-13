import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    visit = [[0] * m for _ in range(n)]
    queue = deque()
    queue.append((0,0))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and graph[ny][nx] == 0 and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                queue.append((ny, nx))
            elif 0<=ny<n and 0<=nx<m and graph[ny][nx] == 1:
                visit[ny][nx] += 1
    for i in range(n):
        for j in range(m):
            if visit[i][j] > 1:
                graph[i][j] = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs()
            cnt += 1
print(cnt)