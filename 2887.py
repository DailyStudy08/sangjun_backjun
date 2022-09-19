import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
node_v = []
for i in range(1, n+1):
    x, y, z = (map(int, input().split()))
    node_v.append((i , x, y, z))

edges = []
for i in [1,2,3]:
    sort = sorted(node_v, key = lambda x: x[i])  
    print(sort)
    e = [(abs(b[i] - a[i]), a[0], b[0]) for a, b in zip(sort[:-1], sort[1:])]
    print(e)
    edges += e

edges.sort()
print(edges)
# 당연히 100000*100000으로 시간초과
# graph = []

# for i in range(1, n+1):
#     for j in range(i+1, n+1):
#         if i == j:
#             continue
#         if len(graph) <= n+1:
#             value = min(abs(node_v[i][1] - node_v[j][1]), abs(node_v[i][2] - node_v[j][2]), abs(node_v[i][0] - node_v[j][0]))
#             graph.append((value, i, j))
#             graph.sort()
#         else:
#             value = min(abs(node_v[i][1] - node_v[j][1]), abs(node_v[i][2] - node_v[j][2]), abs(node_v[i][0] - node_v[j][0]))
#             if value > graph[-1][0]:
#                 continue
#             for k in range(len(graph)):
#                 if graph[k][0] > value:
#                     graph[k] = (value, i, j)
#                     break

parents = [i for i in range(n+1)]

def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parents(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

total_cost = 0
for i in edges:
    if find_parents(parents, i[1]) != find_parents(parents, i[2]):
        union_parents(parents, i[1], i[2])
        total_cost += i[0]
print(total_cost)