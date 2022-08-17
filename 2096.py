import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
max_result = [0]*3
min_result = [0]*3
max_dp = [0]*3
min_dp = [0]*3

for j in range(0, n):
    a, b, c =map(int, input().split())
    for k in range(3):
        if k == 0:
            max_dp[0] = a + max(max_result[k], max_result[k+1])
            min_dp[0] = a + min(min_result[k], min_result[k+1])
        if k == 1:
            max_dp[1] = b + max(max_result[k], max_result[k+1], max_result[k-1])
            min_dp[1] = b + min(min_result[k], min_result[k+1], min_result[k-1])
        if k == 2:
            max_dp[2] = c + max(max_result[k], max_result[k-1])
            min_dp[2] = c + min(min_result[k], min_result[k-1])
    for k in range(3):
        max_result[k] = max_dp[k]
        min_result[k] = min_dp[k]
print(max(max_result), min(min_result))