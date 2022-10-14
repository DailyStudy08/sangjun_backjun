from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int,input().split())
graph = []
for _ in range(n):
    arr = list(input())
    graph.append(arr)

def bfs():
    q = deque()
    q.append((0, 0, 1, graph[0][0]))
    max_v = 0
    while q:
        y, x, cnt, visited = q.pop()
        if cnt > max_v:
            max_v = cnt
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < n and 0 <= nx < m and not graph[ny][nx] in visited:
                q.append((ny, nx, cnt + 1, visited+graph[ny][nx]))
    return max_v

print(bfs())