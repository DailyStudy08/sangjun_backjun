import heapq
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
    
def prim(start):
    v = []
    visit = [0] * (n+1)
    q = []
    for i in graph[start]:
        heapq.heappush(q, i)
    total = 0
    visit[start] = 1
    while q:
        c, node = heapq.heappop(q)
        if visit[node] == 0:
            visit[node] = 1
            v.append(c)
            total += c
            for edge in graph[node]:
                if visit[edge[1]] == 0:
                    heapq.heappush(q, edge)
    return v
# sort: 프림은 추가되는 순서가 작은 순대로가 아니기때문
print(sum(sorted(prim(1))[:-1:]))
        

# parents = [i for i in range(n+1)]
# road = []
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     road.append((c, a, b))
# road.sort()

# def find_p(parents, x):
#     if parents[x] != x:
#         parents[x] = find_p(parents, parents[x])
#     return parents[x]

# def union_p(parents, a, b):
#     a = find_p(parents, a)
#     b = find_p(parents, b)
#     if a < b:
#         parents[b] = a
#     else:
#         parents[a] = b

# min_v = []
# for i in range(m):
#     c, a, b = road[i]
#     if find_p(parents, a) != find_p(parents, b):
#         union_p(parents, a, b)
#         min_v.append(c)
    
# print(sum(min_v[:-1]))