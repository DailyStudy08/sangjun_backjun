s = []
result = []
def bfs():
    if len(s) == 10:
        return
    for i in range(10):
        if s and s[-1] >= i:
            continue
        s.append(i)
        result.append(int(''.join(map(str, s[::-1]))))
        bfs()
        s.pop()
bfs()
result.sort()
print(len(result))
n = int(input())
if len(result)>n:
    print(result[n])
else:
    print(-1)