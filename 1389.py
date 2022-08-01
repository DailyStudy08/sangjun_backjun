import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

node, line = map(int, input().split())
graph = [[]for i in range(node+1)]
result = []
for _ in range(line):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))
for i in graph:
    i.sort()

def bfs(starting, visited, graph):
    queue = deque(graph[starting])
    visited[starting] = True
    while queue:
        a, cnt = queue.popleft()
        if floid[a] > cnt:
            floid[a] = cnt
        visited[a] = True
        for i in graph[a]:
            if visited[i[0]] == False:
                queue.append((i[0], cnt+1))
for i in range(1, node+1):
    visited = [False for i in range(node+1)]
    floid = [99999 for i in range(node+1)]
    bfs(i, visited, graph)
    result.append(sum(floid)-99999*2)      
print(result.index(min(result))+1)
