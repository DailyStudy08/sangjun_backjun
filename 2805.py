import sys
sys.stdin = open('input.txt', 'r')

wood, home = map(int, input().split())
wood_lst = list(map(int, input().split()))
wood_sum = sum(wood_lst)
start = 0
end = max(wood_lst)
while start <= end:
    cnt = 0
    mid = int((start + end)/2)
    for i in wood_lst:
        if i > mid:
            cnt += i - mid
    if cnt >= home:
        start = mid + 1
    else:
        end = mid - 1
print(end)
