n, m = map(int,input().split())
s = []
visited = [False] * (n+1)
results = []
def dfs():
    if len(s) == m and not set(s) in results:
        results.append(set(s))
        print(' '.join(map(str, s)))
        return
    else:
        for i in range(1, n+1):
            if visited[i]:
                continue
            s.append(i)
            visited[i] = True
            dfs()
            s.pop()
            visited[i] = False
dfs()