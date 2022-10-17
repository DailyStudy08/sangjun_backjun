def solution(m, n, board):
    answer = 0
    graph = []
    for i in range(m):
        graph.append(list(board[i]))
    temp = True
    while temp == True:
        block = set()
        for i in range(m-1):
            for j in range(n-1):
                if graph[i][j] != 0 and graph[i][j] == graph[i+1][j] == graph[i][j+1] == graph[i+1][j+1]:
                    block.add((i, j))
                    block.add((i+1, j))
                    block.add((i, j+1))
                    block.add((i+1, j+1))
        answer += len(block)
        for k in block:
            y, x = k
            graph[y][x] = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if graph[i][j] == 0:
                    for k in range(i, -1, -1):
                        if graph[k][j] != 0:
                            graph[i][j], graph[k][j] = graph[k][j], graph[i][j]
                            break
        # print(block)
        if not block:
            temp = False
        # for i in graph:
        #     print(i)
        # print("-----")
    return answer
m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

print(solution(m, n, board))