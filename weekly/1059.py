import sys
sys.stdin = open('input.txt','r')

list_big = int(input())
set_s = list(map(int, input().split()))
n = int(input())
set_s.append(n)
set_s.sort()
n_index = set_s.index(n)
cnt = 0
if n_index != 0:
    for i in range(set_s[n_index-1]+1, set_s[n_index+1]):
        for j in range(set_s[n_index-1]+1, set_s[n_index+1]):
            if i < j and i <= n <= j:
                cnt += 1
else:
    for i in range(1, set_s[1]):
        for j in range(1, set_s[1]):
            if i < j and i <= n <= j:
                cnt += 1
print(cnt)
