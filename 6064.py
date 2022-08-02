import sys
sys.stdin = open('input.txt', 'r')

# 공배수 까지 for문 돌리면서 m, n로 나눴을때 나머지가 x, y인 수
test = int(input())
for _ in range(test):
    m, n, x, y = map(int, input().split())
    i, j = 0, 0
    while True:
        if m*i + x == n*j + y:
            print(m*i + x)
            break
        elif m*i + x > m*n or n*j + y > m*n:
            print(-1)
            break
        elif m*i + x < n*j + y:
            i += 1
        elif m*i + x > n*j + y:
            j += 1
        
# 시간초과
# test = int(input())
# for _ in range(test):
#     m, n, x, y = map(int, input().split())
#     month_lst = []
#     inka_year, inka_month = 1, 1
#     while True:
#         if inka_year == m and inka_month == n:
#             month_lst.append((m, n))
#             break
#         if inka_year <= m and inka_month <= n:
#             month_lst.append((inka_year, inka_month))
#         elif inka_year > m:
#             inka_year = 1
#             month_lst.append((inka_year, inka_month))
#         elif inka_month > n:
#             inka_month = 1
#             month_lst.append((inka_year, inka_month))
#         inka_year += 1
#         inka_month += 1
#     if (x, y) in month_lst:
#         print(month_lst.index((x, y))+1)
#     else:
#         print(-1)