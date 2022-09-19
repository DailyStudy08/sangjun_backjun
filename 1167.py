from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
graph =[[]for _ in range(n+1)]
for _ in range(n):
    a, *b, end = map(int, input().split())
    for i in range(0, len(b), 2):
        graph[a].append((b[i], b[i+1]))
        graph[b[i]].append((a, b[i+1]))

def dfs(start):
    q = deque()
    q.append((start, 0))
    max_v = 0
    max_i = 0
    visit = [0] *(n+1)
    visit[start] = 1
    while q:
        node, value = q.pop()
        if value > max_v:
            max_v = value
            max_i = node
        for new_node, cost in graph[node]:
            if visit[new_node] != 1:
                q.append((new_node, value+cost))
                visit[new_node] = 1
    return max_v, max_i

a, b = dfs(1)
c, d = dfs(b)
print(c)