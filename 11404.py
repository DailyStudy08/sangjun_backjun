import sys
sys.stdin = open('input.txt', 'r')

from math import inf

node = int(input())
line = int(input())
graph = [[inf for _ in range(node)] for _ in range(node)]
for _ in range(line):
    i, j, value = map(int, input().split())
    graph[i-1][j-1] = min(graph[i-1][j-1], value)

for i in range(node):
    graph[i][i] = 0

for i in range(node):
    for j in range(node):
        for k in range(node):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
for i in range(node):
    for j in range(node):
        if graph[i][j] == inf:
            graph[i][j] = 0
for i in graph:
    print(*i)