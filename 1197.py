import heapq
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
v, e = map(int, input().split())

# # kruskal union find 알고리즘을 활용
# total_cost = 0
# graph = []
# parent = [i for i in range(v+1)]
# # 간선을 비용순으로 정렬
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     graph.append((c, a, b))
# graph.sort()

# # 부모찾는 알고리즘 find
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# # 만약 부모가 같다면 큰걸로 통합 union
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# for i in range(e):
#     cost, a, b = graph[i]
#     # 부모가 다르면 최소 신장트리에 포함
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         total_cost += cost
        
# print(total_cost)

# prim algorithm
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
    

def prim(start):
    visit = [0] * (v+1)
    q = []
    for i in graph[start]:
        heapq.heappush(q, i)
    mst = [start]
    total_cost = 0
    visit[start] = 1
    while q:
        
        c, node = heapq.heappop(q)
        if visit[node] == 0:
            visit[node] = 1
            mst.append(node)
            total_cost += c
            
            for edge in graph[node]:
                if visit[edge[1]] == 0:
                    heapq.heappush(q, edge)
    return total_cost
print(prim(1))