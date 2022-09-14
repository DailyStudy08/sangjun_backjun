import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque


n = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
end_node = []


for i in range(n+1):
    if len(graph[i]) == 1:
        end_node.append(i)
        
def dfs(start):
    visit = [0]*(n+1)
    s = deque(graph[start])
    visit[start] = 1
    maxi = 0
    maxi_node = 0
    while s:
        node, cost = s.pop()
        visit[node] = 1
        if cost > maxi:
            maxi = cost
            maxi_node = node
        for new_node, new_cost in graph[node]:
            if visit[new_node] == 0:
                s.append((new_node, new_cost + cost))
                visit[new_node] = 1
    return maxi, maxi_node


#     return maxi
# result = []
# for i in end_node:
#     result.append(dfs(i))
# print(result)
# print(max(result) if result else 0)


first = dfs(1)
second = dfs(first[1])

print(second[0])