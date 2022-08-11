import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[(0, 0) for _ in range(n)] for _ in range(k+1)]
for i in range(n):
    w, v = map(int, input().split())
    arr[w][i] = (w, v)
for y in range(1, k+1):
    for i in range(n):
        up_weight = arr[y-1][i][0]
        if arr[y-1][i] == (0, 0):
            continue
        result = 0
        result += arr[y-up_weight][i][1]
        max_v = 0
        for j in range(n):
            if max_v < arr[y-up_weight][j][1]:
                max_v = arr[y-up_weight][j][1]
        result += max_v
        if result > arr[y-1][i][1]:
            arr[y][i] = (up_weight, result)
        else:
            arr[y][i] = (up_weight, arr[y-1][i][1])
max_v = 0
for i in arr[y]:
    if max_v < i[1]:
        max_v = i[1]
print(max_v)

# things, weight = map(int, input().split())
# t_lst = []
# for i in range(things):
#     w, v = map(int, input().split())
#     t_lst.append((w, v))
# n = len(t_lst)
# t_lst.sort()
# visit = [False]*(n)
# s = []
# result = []
# def combi():
#     for i in range(n):
#         if visit[i] == True:
#             continue
#         if s and s[-1] > t_lst[i]:
#             continue
#         s.append(t_lst[i])
#         visit[i] = True
#         result.append(s[:])
#         combi()
#         s.pop()
#         visit[i] = False
# combi()
# max_v = 0
# for j in result:
#     wei = 0
#     vel = 0
#     for k in j:
#         wei += k[0]
#         vel += k[1]
#         if wei > weight:
#             break
#     if wei <= weight and vel > max_v:
#         max_v = vel
# print(max_v)