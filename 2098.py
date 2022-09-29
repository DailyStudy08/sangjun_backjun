import sys
sys.stdin = open('input.txt')
INF = 1e9
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (1<<n) for _ in range(n)]

def dfs(x, visited):
    if visited == (1 << n) - 1:
        if graph[x][0] == 0:
            return INF
        dp[x][visited] = graph[x][0]
        return graph[x][0]
    
    if dp[x][visited] != 0:
        return dp[x][visited]
    
    min_dist = INF
    for i in range(n):
        if not visited & (1 << i) and graph[x][i] != 0:
            min_dist = min(min_dist, dfs(i, visited | (1 << i)) + graph[x][i])
            
    dp[x][visited] = min_dist
    return min_dist
print(dfs(0, 1))
print(dp)

# cnt = 0
# min_v = 1e9
# bina = bin(2**(n)-1)
# def dfs(k):
#     global min_v, cnt, visited
#     if not ~visited & int(bina, 2):
#         if min_v > cnt + graph[k][0]:
#             min_v = cnt+graph[k][0]
#         return
#     if cnt >= min_v:
#         return
#     for i in range(n):
#         if visited & (1<<i):
#             continue
#         cnt += graph[k][i]
#         if cnt >= min_v:
#             cnt -= graph[k][i]
#             continue
#         visited = visited | (1<<i)
#         dfs(i)
#         visited = ~(~visited | (1<<i))
#         cnt -= graph[k][i]