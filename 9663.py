def possible(m):
    for i in range(m):
        if graph[m] == graph[i] or abs(graph[m] - graph[i]) == abs(m - i):
            return False
    return True

def queen(m):
    global cnt
    if n == m:
        print(graph)
        cnt += 1
        return
    else:
        for i in range(n):
            graph[m] = i
            if possible(m):
                queen(m+1)

n = int(input())
cnt = 0
graph = [0] * (n)
queen(0)
print(cnt)