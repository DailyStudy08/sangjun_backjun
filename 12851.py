from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bfs(a, b):
    fastest = 1e9
    path = 0
    queue = deque()
    queue.append((a, 0))
    while queue:
        x, sec = queue.popleft()
        if x == b:
            if sec < fastest:
                fastest = sec
                path = 0
                path += 1
            elif sec == fastest:
                path += 1
        visit[x] = 1
        for i in [1, -1, x]:
            nx = x + i
            if 0<=nx<100001 and visit[nx] >= sec:
                queue.append((nx, sec+1))
                visit[nx] = sec+1
    return fastest, path
a, b = map(int, input().split())
visit = [1e9] * 100001
for i in bfs(a, b):
    print(i)