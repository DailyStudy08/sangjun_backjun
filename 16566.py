import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def find_p(x):
    if x != parents[x]:
        parents[x] = find_p(parents[x])
    return parents[x]

n, m, k = map(int, input().split())
minsu = list(map(int, input().split()))
chulsu = list(map(int, input().split()))
minsu.sort()
def binary(target):
    start = 0
    end = m-1
    while start <= end:
        mid = (start + end) // 2
        if target < minsu[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start

parents = [i for i in range(m)]
print(minsu)
for i in chulsu:
    num = binary(i)
    p = find_p(num)
    if num == find_p(num):
        print(minsu[p])
        parents[num] = num+1
    else:
        print(minsu[p])
        parents[p] = p + 1
    print(parents)
    