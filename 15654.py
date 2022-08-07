import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []
visit = [False] * 10001
def back():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    else:
        for i in nums:
            if visit[i]:
                continue
            result.append(i)
            visit[i] = True
            back()
            result.pop()
            visit[i] = False

back()