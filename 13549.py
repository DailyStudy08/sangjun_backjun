from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(a, b):
    queue = deque()
    queue.append((a, 0))
    while queue:
        x, sec = queue.popleft()
        if x == b:
            return sec
        visit[x] = 1
        for i in [1, -1, x]:
            nx = x + i
            if 0<=nx<100001 and visit[nx] == 0:
                if i == x:
                    queue.appendleft((nx, sec))
                else:
                    queue.append((nx, sec+1))
                visit[nx] = 1
a, b = map(int, input().split())
visit = [0] * 100001
print(bfs(a, b))