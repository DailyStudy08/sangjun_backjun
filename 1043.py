from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
nt, *true = map(int, input().split())
graph = [[] for _ in range(n+1)]
party = []
for _ in range(m):
    p, *people = map(int, input().split())
    if p != 1:
        for i in people:
            for j in people:
                if i != j:
                    graph[i].append(j)
    party.append(people)
def bfs(li):
    visited = [0] * (n+1)
    queue = deque(li)
    while queue:
        q = queue.popleft()
        visited[q] = 1
        if q in true:
            return 0
        for i in graph[q]:
            if visited[i] == 0:
                queue.append(i)
    return 1
cnt = 0
for i in party:
    cnt += bfs(i)
print(cnt)
