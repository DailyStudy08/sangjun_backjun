import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque


def dfs(start):
    global cnt
    y, x, d = start
    if y == n-1 and x == n-1:
        cnt += 1
        return
    
    if y+1 < n and x+1 < n:
        if graph[y+1][x+1] == 0 and graph[y][x+1] == 0 and graph[y+1][x] == 0:
            dfs((y+1, x+1, 2))
    if d == 0 or d == 2:
        if x+1 < n:
            if graph[y][x+1] == 0:
                dfs((y, x+1, 0))
                
    if d == 1 or d == 2:
        if y+1 < n:
            if graph[y+1][x] == 0:
                dfs((y+1, x, 1))

n = int(input())
graph = [[] for _ in range(n)]
cnt = 0
for i in range(n):
    graph[i] = list(map(int, input().split()))
    
dfs((0, 1, 0))

print(cnt)
                