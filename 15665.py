import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []
printing = set()
def back():
    if len(result) == m:
        printing.add(tuple(result))
        return
    else:
        for i in nums:
            result.append(i)
            back()
            result.pop()

back()
for i in sorted(list(printing)):
    print(' '.join(map(str, i)))