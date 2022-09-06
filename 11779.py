import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = 117440512

graph = [[] for _ in range(n+1)]
for _ in range(m):
    st, ed, t = map(int,input().split())
    graph[st].append((ed, t))
start, end = map(int,input().split())

distance = [INF] * (n+1)

def djaikstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, [start, [start]]))
    result = [start]
    while q:
        dist, node = heapq.heappop(q)
        if dist < distance[node[0]]:
            continue
        if node[0] == end:
            break
        for next in graph[node[0]]:
            cost = next[1] + distance[node[0]]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                a = node[1]+[next[0]]
                heapq.heappush(q, (cost, [next[0], a]))
                if next[0] == end:
                    result = a
        print(q)
    return result
ans = djaikstra(start)
print(distance[end])
print(len(ans))
for i in ans:
    print(i, end=' ')