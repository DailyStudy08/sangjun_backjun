import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq
INF = sys.maxsize
v, e = map(int, input().split())
start = int(input())
graph = [[]for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
distance = [INF] * (v+1)

def daik(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for n in graph[node]:
            cost = dist + n[1]
            if distance[n[0]] > cost:
                distance[n[0]] = cost
                heapq.heappush(q, (cost, n[0]))

daik(start)
for i in range(1, v+1):
    if distance[i] >= INF:
        print('INF')
    else:
        print(distance[i])