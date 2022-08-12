import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def go(my, mx, color, no_color):
    lst = []
    for i in range(8):
        nx = mx
        ny = my
        for _ in range(n):
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == color:
                lst.append((ny, nx, i))
                break
            elif 0 <= nx < n and 0 <= ny < n and board[ny][nx] == no_color:
                continue
            elif 0 <= nx < n and 0 <= ny < n and board[ny][nx] == 0:
                break
    return lst

def reverse(y, x, lst, color):
    for i in lst:
        lx, ly = x, y
        ny, nx, value = i
        while not(ly == ny and lx == nx):
            ly = ly + dy[value]
            lx = lx + dx[value]
            board[ly][lx] = color
test = int(input())
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for t in range(1, test+1):
    n, m = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[n//2][n//2] = 2
    board[n//2-1][n//2-1] = 2
    board[n//2-1][n//2] = 1
    board[n//2][n//2-1] = 1
    for _ in range(m):
        y, x, color = map(int, input().split())
        y -= 1
        x -= 1
        if color == 1:
            board[y][x] = 1
            lst = go(y, x, color, 2)
            reverse(y, x, lst, 1)
        else:
            board[y][x] = 2
            lst = go(y, x, color, 1)
            reverse(y, x, lst, 2)
    b_cnt = 0
    w_cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                b_cnt += 1
            elif board[i][j] == 2:
                w_cnt += 1
    print(f'#{t} {b_cnt} {w_cnt}')
