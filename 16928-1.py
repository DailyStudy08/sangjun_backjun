import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

ladder = [[0, 1000] for _ in range(101)]

sadari, snake = map(int, input().split())
for _ in range(sadari+snake):
    start, end = map(int, input().split())
    ladder[start][0] = end

def ls(start):
    queue = deque([(start, 0)])
    while queue:
        v, cnt = queue.popleft()
        if v == 100:
            return cnt
        for i in range(v+1, v+7):
            if i <= 100 and ladder[i][1] > cnt:
                if ladder[i][0] > 0:
                    queue.append((ladder[i][0], cnt+1))
                else:
                    queue.append((i, cnt+1))
                ladder[i][1] = cnt
print(ls(1))
            