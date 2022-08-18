import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

block_i = [[0, 0, -1, -1], [0, -1, -1, -2], [0, -1, -1, -2], [0, 0, -1, -1], [0, 0, -1, -1]]      #  노란색, 초록색(4) 테트로미노
block_j = [[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, -1, -1], [0, 1, 0, -1], [0, 1, 1, 2]]

max_total = 0
for i in range(n):
    for j in range(m):
        for block in range(5):
            total = 0
            for k in range(4):
                ni = i + block_i[block][k]
                nj = j + block_j[block][k]
                if 0 <= ni < n and 0 <= nj < m:
                    total += arr[ni][nj]
                    if total > max_total:
                        max_total = total

# 파랑, 주황, 핑크 - 세개짜리 막대기 두고 한개씩 붙이기(가로)
di = [1, 1, 1, 0, -1, -1, -1]
dj = [0, 1, 2, 3, 2, 1, 0]

for i in range(n):
    for j in range(m):
        for k in range(7):
            total2 = 0
            plus = 0
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and 0 <= j+2 < m:
                plus = arr[ni][nj]
                total2 += plus + sum(arr[i][j:j + 3])
                if total2 > max_total:
                    max_total = total2

# 파랑, 주황, 핑크 - 세개짜리 막대기 두고 한개씩 붙이기(세로)
ci = [0, 1, 2, 3, 2, 1, 0]
cj = [1, 1, 1, 0, -1, -1, -1]
for i in range(n):
    for j in range(m):
        for k in range(7):
            total3 = 0
            plus3 = 0
            nni = i + ci[k]
            nnj = j + cj[k]
            if 0 <= nni < n and 0 <= nnj < m and 0 <= i+2 < n:
                plus3 = arr[nni][nnj]
                total3 += plus3 + (arr[i][j] + arr[i + 1][j] + arr[i + 2][j])
                if total3 > max_total:
                    max_total = total3

print(max_total)