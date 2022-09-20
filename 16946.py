from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    arr = list(input().strip())
    arr = list(map(int, arr))
    graph.append(arr)
visit = [[0 for _ in range(m)]for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def break_wall(start):
    cnt = 1
    wall = []
    q = deque()
    q.append(start)
    y, x = start
    visit[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and visit[ny][nx] == 0 and graph[ny][nx] == 0:
                q.append((ny, nx))
                cnt += 1
                visit[ny][nx] = 1
            elif 0<=ny<n and 0<=nx<m and visit[ny][nx] == 0 and graph[ny][nx] != 0:
                wall.append((ny, nx))
                visit[ny][nx] = 1
    for ky, kx in wall:
        visit[ky][kx] = 0
        graph[ky][kx] += cnt

for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and graph[i][j] == 0:
            break_wall((i, j))
for i in range(len(graph)):
    for j in graph[i]:
        print(j%10, end='')
    if i != len(graph)-1:
        print()