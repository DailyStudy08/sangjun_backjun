from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
graph = [list(map(int,input().split()))for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sy = i
            sx = j
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def babyshark(sy, sx):
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[sy][sx] = True
    graph[sy][sx] = 0
    size = 2
    exp = 0
    distance = 0
    queue = deque()
    moving = []
    queue.append((sy, sx, 0))
    while queue:
        y, x, d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[ny][nx] <= size and visited[ny][nx] == False:
                if graph[ny][nx] != 0 and graph[ny][nx] < size:
                    moving.append((ny, nx, d+1))
                else:
                    queue.append((ny, nx, d+1))
                visited[ny][nx] = True
        if not queue and moving:
            moving.sort(key = lambda x :(x[2], x[0], x[1]), reverse = True)
            ny, nx, d = moving.pop()
            queue.append((ny, nx, d))
            distance = d
            exp += 1
            if exp == size:
                size += 1
                exp = 0
            graph[ny][nx] = 0
            visited = [[False for _ in range(n)] for _ in range(n)]
            moving = []
    return distance
print(babyshark(sy, sx))