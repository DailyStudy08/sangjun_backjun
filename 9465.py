import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    dp = [[0 for _ in range(n)]for i in range(2)]
    for i in range(2):
        arr.append(list(map(int, input().split())))
    for i in range(n):
        if i == 0:
            dp[0][i] = arr[0][i]
            dp[1][i] = arr[1][i]
        elif i == 1:
            dp [0][i] = arr[1][0] + arr[0][i]
            dp [1][i] = arr[0][0] + arr[1][i]
        else:
            dp[0][i] = arr[0][i] + max(dp[0][i-2], dp[1][i-1], dp[1][i-2])
            dp[1][i] = arr[1][i] + max(dp[1][i-2], dp[0][i-1], dp[0][i-2])
    print(max(dp[0][n-1], dp[1][n-1]))