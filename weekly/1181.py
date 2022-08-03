n = int(input())
N = []
for i in range(n):
    a = list(map(str, input()))
    N.append(a)
N.sort(key = lambda x:(len(x), x))
for i in range(0, n-1):
    if N[i] == N[i+1]:
        N[i] = 0
while 0 in N:
    N.remove(0)
for i in N:
    print(*i, sep="")