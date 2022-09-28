import sys
sys.stdin = open('input.txt', 'r')
import heapq
from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
island = [[0 for _ in range(m)] for _ in range(n)]

def island_num(y, x, num):
    q = deque()
    q.append((y, x))
    island[y][x] = num
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                island[ny][nx] = num
                q.append((ny, nx))
                
cnt = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            island_num(i, j, cnt)
            cnt += 1

def bridge(y, x, i_num):
    q = deque()
    for i in range(4):
        q.append((y, x, i, 0))
    while q:
        y, x, i, cnt = q.pop()
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= ny < n and 0 <= nx < m and island[ny][nx] != i_num:
            if island[ny][nx] != 0:
                if cnt > 1:
                    graph[i_num].append((cnt, island[ny][nx]))
                continue
            q.append((ny, nx, i, cnt+1))

graph = [[] for _ in range(cnt)]
for i in range(n):
    for j in range(m):
        if island[i][j] != 0:
            bridge(i, j, island[i][j])
            
def prim(start):
    visit = [0] * (cnt)
    q = []
    for i in graph[start]:
        heapq.heappush(q, i)
    mst = [start]
    total_cost = 0
    visit[start] = 1
    while q:
        
        c, node = heapq.heappop(q)
        if visit[node] == 0:
            visit[node] = 1
            mst.append(node)
            total_cost += c
            
            for edge in graph[node]:
                if visit[edge[1]] == 0:
                    heapq.heappush(q, edge)
    if visit[1:] == [1] * (cnt-1):
        return total_cost
    else:
        return -1

print(prim(1))