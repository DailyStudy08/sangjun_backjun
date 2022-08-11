import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from cmath import inf
import heapq


city = int(input())
node = int(input())
graph = [[]for _ in range(city+1)]
visit = [False]*(city+1)
distance = [inf]*(city+1)

for i in range(node):
    st, ed, co = map(int, input().split())
    graph[st].append((co, ed))

def daik(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
start, end = map(int, input().split())
daik(start)
print(distance[end])