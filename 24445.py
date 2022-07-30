import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(visited, start, graph):
    cnt = 0
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if visited[v] == 0:
            cnt += 1
            visited[v] = cnt
            queue.extend(graph[v])
                
node, line, starting_point = map(int, input().split())
visited = [0] * (node+1)
graph = [[] for _ in range(node+1)]
for _ in range(line):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(node+1):
    graph[i].sort(reverse=True)
bfs(visited, starting_point, graph)
for i in range(1, node+1):
    print(visited[i])