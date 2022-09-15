from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bfs(start):
    global key, paper, go
    go = False
    visit = [[0 for _ in range(w+2)]for _ in range(h+2)]
    q = deque()
    q.append(start)
    visit[0][0] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<h+2 and 0<=nx<w+2 and graph[ny][nx] != '*' and visit[ny][nx] == 0:
                if graph[ny][nx].isupper():
                    if graph[ny][nx].lower() in key:
                        q.append((ny, nx))
                        visit[ny][nx] = 1
                    else:
                        continue
                elif graph[ny][nx].islower():
                    q.append((ny, nx))
                    visit[ny][nx] = 1
                    key += graph[ny][nx]
                    graph[ny][nx] = '.'
                    go = True
                elif graph[ny][nx] == '$':
                    q.append((ny, nx))
                    visit[ny][nx] = 1
                    graph[ny][nx] = '.'
                    paper += 1
                else:
                    q.append((ny, nx))
                    visit[ny][nx] = 1
                


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



tc = int(input())
for t in range(tc):
    h, w = map(int,input().split())
    graph = []
    graph.append(['.']*(w+2))
    for _ in range(h):
        row = ['.']
        row.extend(list(input().strip()))
        row.append('.')
        graph.append(row)
    graph.append(['.']*(w+2))
    key = input()
    start = (0, 0)
    paper = 0
    go = True
    while go:
        bfs(start)
    print(paper)