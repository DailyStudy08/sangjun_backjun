n, m = map(int, input().split())
lst = []

def bfs():
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    else:
        for i in range(1, n+1):
            if lst:
                if lst[-1] > i:
                    continue
            lst.append(i)
            bfs()
            lst.pop()
bfs()