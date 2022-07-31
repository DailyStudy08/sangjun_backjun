import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
# bfs로 순회하면서 날짜 하나씩 더해주는 함수
def tomato(starting):
    queue = deque(starting)
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    while queue:
        y, x, days = queue.popleft()
        visited[y][x] = True
        graph[y][x] = days
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 조건에서 -1만 넣으면 모든게 1일때 문제발생
            # 따라서 1까지 조건에 넣어줌
            if -1< ny < column and -1 < nx < row and visited[ny][nx] == False and graph[ny][nx] != -1 and graph[ny][nx] != 1:
                queue.append((ny, nx, days+1))
                visited[ny][nx] = True
# 결과 출력 함수
def result():
    maxi = 0
    for i in range(column):
        for j in range(row):
            if graph[i][j] == 0:
                return -1
            elif maxi < graph[i][j]:
                maxi = graph[i][j]
    return maxi - 1

row, column = map(int, input().split())
graph = []
visited = [[False for _ in range(row)]for _ in range(column)]
start = []
for _ in range(column):
    graph.append(list(map(int, input().split())))
for i in range(column):
    for j in range(row):
        if graph[i][j] == 1:
            start.append((i, j, 1))
tomato(start)
print(result())