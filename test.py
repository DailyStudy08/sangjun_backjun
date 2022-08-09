import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    count = [0] * 101
    n = int(input())
    arr = list(map(int, input().split()))
    for i in arr:
        count[i] += 1
    for k in range(n):
        for i in range(1, 100):
            if count[i] != 0:
                count[i], count[i+1] = count[i]-1, count[i+1] +1
                break
        for i in range(1,100):
            if count[-i] != 0:
                count[-i], count[-i-1] = count[-i]-1, count[-i-1] +1
                break
    for i in range(101):
        if count[i] != 0:
            min_v = i
            break
    for i in range(1, 101):
        if count[-i] != 0:
            max_v = 100-i+1
            break
    print(f'#{t} {max_v-min_v}')