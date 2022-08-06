import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque
# 가장 짧은 연산을 visit에 넣어줌
# rotate말고 수식으로 표현하자... 시간초과의 원인이었다.
# bfs는 최단거리를 찾을 수 있으니까 다른 방향으로 갔을 때 큰 경우는 찾지 않아도 좋다. (뱀과 사다리가 아니니까...)
def dslr():
    queue = deque([[start, '']])
    while queue:
        a , b = queue.popleft()
        if a == end:
            return b
        d = (a * 2) % 10000
        if not visit[d]:
            visit[d] = b + 'D'
            queue.append([d, b + 'D'])
        s = a - 1 if a - 1 >= 0 else 9999
        if not visit[s]:
                visit[s] = b + 'S'
                queue.append([s, b + 'S'])
        l = 10*(a%1000) + a//1000
        r = 1000*(a%10) + a//10
        if not visit[r]:
            visit[r] = b + 'R'
            queue.append([r, b + 'R'])
        if not visit[l]:
            visit[l] = b + 'L'
            queue.append([l, b + 'L'])
        
t = int(input())
for _ in range(t):
    visit = [''] * 10000
    start, end = map(int, input().split())
    print(dslr())