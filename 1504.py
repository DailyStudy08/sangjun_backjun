import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
import heapq

n, e = map(int, input().split())
graph = [[]for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
node1, node2 = map(int, input().split())


def daik(start, end):
    distance = [1e9] * (n+1)
    h = []
    heapq.heappush(h, (start, 0))
    distance[start] = 0
    while h:
        node, dist = heapq.heappop(h)
        if dist > distance[node]:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (i[0], cost))
    return distance[end]

result = min(daik(1, node1) + daik(node1, node2) + daik(node2, n), daik(1, node2) + daik(node2, node1) + daik(node1, n))
if result >= 1e9:
    print(-1)
else:
    print(result)