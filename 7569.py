import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def three_bfs(starting):
    queue = deque(starting)
    dz = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dx = [0, 0, 0, 0, 1, -1]
    while queue:
        z, y, x, days = queue.popleft()
        visited[z][y][x] == True
        graph[z][y][x] = days
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if -1 < nz < depth and -1 < ny < column and -1 < nx < row and visited[nz][ny][nx] == False and graph[nz][ny][nx] != 1 and graph[nz][ny][nx] != -1:
                queue.append((nz, ny, nx, days+1))
                visited[nz][ny][nx] = True
def result():
    maxi = 0
    for k in range(depth):
        for i in range(column):
            for j in range(row):
                if graph[k][i][j] == 0:
                    return -1
                elif maxi < graph[k][i][j]:
                    maxi = graph[k][i][j]
    return maxi - 1

row, column, depth = map(int, input().split())
graph = []
visited = [[[False for _ in range(row)]for _ in range(column)]for _ in range(depth)]
start = []

for i in range(depth):
    z_axis = []
    for j in range(column):
        z_axis.append(list(map(int, input().split())))
    graph.append(z_axis)

for l in range(depth):
    for k in range(column):
        for m in range(row):
            if graph[l][k][m] == 1:
                start.append((l, k, m, 1))
three_bfs(start)
print(result())