import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def go(y, x, color, no_color):
    lst = []
    for i in range(8):
        for j in range(n):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == color:
                lst.append((ny, nx, i))
                break
            elif 0 <= nx < n and 0 <= ny < n and board[ny][nx] == no_color:
                x = nx
                y = ny
            else:
                break
    return lst

def reverse(lst, color):
    for i in lst:
        ny, nx, value = i
        if value == 0:
            for q in range(ny+1, n):
                board[ny+q][nx] = color
        elif value == 1:
            for q in range(ny+1, y):
                for w in range(x+1, nx):
                    if q == -(w):
                        board[ny+q][x+w] = color
        elif value == 2:
            for w in range(x+1, nx):
                board[ny][x+w] = color
        elif value == 3:
            for q in range(y+1, ny):
                for w in range(x+1, nx):
                    if q == w:
                        board[y+q][x+w] = color
        elif value == 4:
            for q in range(y+1, ny):
                board[y+q][nx] = color
        elif value == 5:
            for q in range(y+1, ny):
                for w in range(nx+1, x):
                    if q == -(w):
                        board[y+q][nx+w] = color
        elif value == 6:
            for w in range(nx+1, x):
                board[ny][nx+w] = color
        elif value == 7:
            for q in range(ny+1, y):
                for w in range(nx+1, x):
                    if q == w:
                        board[ny+q][nx+w] = color
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
            reverse(lst, 1)
        else:
            board[y][x] = 2
            lst = go(y, x, color, 1)
            reverse(lst, 2)
        print(lst)
        for k in board:
            print(k)
        print('-----')
    b_cnt = 0
    w_cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                b_cnt += 1
            elif board[i][j] == 2:
                w_cnt += 1
    
    print(f'#{t} {b_cnt} {w_cnt}')