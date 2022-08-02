import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
import copy

line = int(input())
# 인식 면적 갯수
cnt_gr = 0
cnt_ngr = 0
graph = []
for i in range(line):
    graph.append(list(input()))
# 적록색맹의 그래프 새로 만들어줌
new_graph = copy.deepcopy(graph)

def green_red(y, x, graph):
    queue = deque([(y, x)])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        y, x = queue.popleft()
        color = graph[y][x]
        graph[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프 벗어나지 않고 방문하지 않고 RGB값이 같다면 큐에 추가
            if -1 < nx < line and -1 < ny < line and graph[ny][nx] == color and graph[ny][nx] != 0:
                queue.append((ny, nx))

for i in range(line):
    for j in range(line):
        if graph[i][j] != 0:
            # 함수가 실행될 때 마다 cnt += 1
            green_red(i, j, graph)
            cnt_ngr += 1
# 적록색맹의 그래프를 새로 그려줌
for i in range(line):
    for j in range(line):
        if new_graph[i][j] == 'R':
            new_graph[i][j] = 'G'

for i in range(line):
    for j in range(line):
        if new_graph[i][j] != 0:
            green_red(i, j, new_graph)
            cnt_gr += 1

print(cnt_ngr, cnt_gr)