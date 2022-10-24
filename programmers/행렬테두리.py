def moving(columns, rows, x1, y1, x2, y2, graph):
    visit = [[0 for _ in range(columns)]for _ in range(rows)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    stack = [(y1, x1)]
    visit[y1][x1] = 1
    minv = 1e9
    moving = -1
    while stack:
        y, x = stack.pop()
        if graph[y][x] < minv:
            minv = graph[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if y1 <= ny <= y2 and x1 <= nx <= x2 and visit[ny][nx] == 0 and (ny == y1 or ny == y2 or nx == x1 or nx == x2):
                visit[ny][nx] = 1
                if (y, x) == (y1, x1):
                    moving = graph[ny][nx]
                    graph[ny][nx] = graph[y][x]
                else:
                    graph[ny][nx], moving = moving, graph[ny][nx]
                stack.append((ny, nx))
                break
    if moving < minv:
        minv = moving
    graph[y1][x1] = moving
    
    return minv
        
def solution(rows, columns, queries):
    answer = []
    graph = [[0 for _ in range(columns)]for _ in range(rows)]

    cnt = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = cnt
            cnt += 1
    for k in queries:
        y1, x1, y2, x2 = k
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        a = moving(columns, rows, x1, y1, x2, y2, graph)
        answer.append(a)
    return answer

rows = 4
columns = 6
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows, columns, queries))