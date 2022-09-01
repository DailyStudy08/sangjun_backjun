from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
# 가로 세로 받아주기
n, m = map(int,input().split())
# 그래프 만들어주기
graph = []
for i in range(n):
    graph.append(list(map(int, list(input()))))

# 방문처리를 부순경우와 부수지 않은 경우로 나누기
visit = [[0 for _ in range(m)] for _ in range(n)]
visit_break = [[0 for _ in range(m)] for _ in range(n)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
# 스타트는 미리 방문
visit[0][0] = 1
visit_break[0][0] = 1
# bfs시작
def crush(start):
    queue = deque()
    queue.append(start)
    while queue:
        y, x, breakable, cnt = queue.popleft()
        # 도착하면 거리를 리턴
        if (y, x) == (n-1, m-1):
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 부순경우와 안 부순 경우로 나눠서 bfs
            if breakable:
                if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == False:
                    if graph[ny][nx] == 1:
                        visit[ny][nx] = 1
                        queue.append((ny, nx, False, cnt + 1))
                    else:
                        visit[ny][nx] = 1
                        queue.append((ny, nx, True, cnt + 1))
            else:
                if 0 <= ny < n and 0 <= nx < m and visit_break[ny][nx] == False and graph[ny][nx] == 0:
                    visit_break[ny][nx] = 1
                    queue.append((ny, nx, False, cnt + 1))
    return -1
        
print(crush((0, 0, True, 1)))
