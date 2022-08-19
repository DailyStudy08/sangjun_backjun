import sys
sys.stdin = open('input.txt')

def dfs(start, graph, visit):
    stack = graph[start]
    while stack:
        v = stack.pop()
        if v == 99:
            return 1
        visit[v] = True
        for i in graph[v]:
            if not visit[i]:
                stack.append(i)
    return 0
        

for t in range(1, 11):
    test, line = map(int, input().split())
    graph = [[] for _ in range(100)]
    visit = [False for _ in range(100)]
    lst = list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        graph[lst[i]].append(lst[i+1])
    print(graph)
    print(f'#{t} {dfs(0, graph, visit)}')