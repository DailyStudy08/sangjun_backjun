import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for i in range(n):
    nums[i] = (nums[i], i)
result = []
printing = set()
visit = [False] * 10001
def back():
    if len(result) == m:
        printing.add(tuple(result))
        return
    else:
        for i in nums:
            a, b = i
            if visit[b]:
                continue
            result.append(a)
            visit[b] = True
            back()
            result.pop()
            visit[b] = False

back()
for i in sorted(list(printing)):
    print(' '.join(map(str, i)))