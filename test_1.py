def othello(y_x, color):
    will_change = [ [] for i in range(8)]
    reversed_color = 2 if color == 1 else 1
    for dir_ in range(8):
        for move in range(N):
            dir_list = [[move + 1,0],[-(move + 1),0],[0,move + 1],[0,-(move + 1)],[move + 1,move + 1],[move + 1,-(move + 1)],[-(move + 1),move + 1],[-(move + 1),-(move + 1)]]
            move_x = dir_list[dir_][0] ; move_y = dir_list[dir_][1]
            if (N - 1) >= (y_x[0] + move_y) >= 0 and (N - 1) >= (y_x[1] + move_x) >= 0:
                if othello_field[y_x[0] + move_y][y_x[1] + move_x] == reversed_color:
                    will_change[dir_].append([y_x[0] + move_y, y_x[1] + move_x, color])
                elif othello_field[y_x[0] + move_y][y_x[1] + move_x] == color:
                    will_change[dir_].append(True)
                    break
                elif othello_field[y_x[0] + move_y][y_x[1] + move_x] == 0:
                    will_change[dir_].append(False)
                    break
        for j in will_change:
            if len(j) != 0 and j[-1] == True:
                othello_field[y_x[0]][y_x[1]] = color
                for i in j[0:(len(j)-1)]:
                    othello_field[i[0]][i[1]] = i[2]
 
T = int(input())
global othello_field
for case in range(T):
    N, M = map(int,input().split())
    black_stone = 0
    white_stone = 0
    othello_field = [[] for _ in range(N)]
    for i in range(N ** 2): othello_field[i//N].insert(i%N,0)
    othello_field[N // 2 - 1][N // 2 - 1] = 2
    othello_field[N // 2 - 1][N // 2] = 1
    othello_field[N // 2][N // 2 - 1] = 1
    othello_field[N // 2][N // 2] = 2
    for rpt in range(M):
        input_othello = list(map(int,input().split()))
        othello((input_othello[1]-1,input_othello[0]-1),input_othello[2])
    for i in range(N):
        black_stone += othello_field[i].count(1)
        white_stone += othello_field[i].count(2)
    print(f'#{case+1} {black_stone} {white_stone}')