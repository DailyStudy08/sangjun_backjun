import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * 1001

for i in arr:
    result = 0
    result = max(dp[0:i])
    dp[i] = result+1

print(max(dp))
