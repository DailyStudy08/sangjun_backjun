import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []
def back():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    else:
        for i in nums:
            if result:
                if result[-1] > i:
                    continue
            result.append(i)
            back()
            result.pop()
back()