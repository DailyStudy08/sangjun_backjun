import sys
sys.stdin = open('input.txt')

n, m, k = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visit = [[0 for _ in range(m)]for _ in range(n)]
visit[n-1][0] = 1
cnt = 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dfs(y, x, c):
    global cnt
    if c == k:
        if (y, x) == (0, m-1):
            cnt += 1
        return
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == '.' and visit[ny][nx] == 0:
            visit[ny][nx] = 1
            dfs(ny, nx, c+1)
            visit[ny][nx] = 0
dfs(n-1, 0, 1)
print(cnt)