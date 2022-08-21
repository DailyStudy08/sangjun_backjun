from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(y, x, m):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((y, x))
    visit[y][x] = 1
    cnt_b = 1
    while queue:
        ly, lx = queue.popleft()
        for k in range(4):
            ny = ly + dy[k]
            nx = lx + dx[k]
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] > m and not visit[ny][nx]:
                queue.append((ny, nx))
                visit[ny][nx] = 1
answer = 0
for m in range(101):
    cnt = 0
    visit = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > m and not visit[i][j]:
                bfs(i, j, m)
                cnt += 1
    if cnt > answer:
        answer = cnt
print(answer)