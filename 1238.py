import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = 1e9
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = []
for _ in range(m):
    st, ed, t = map(int, input().split())
    graph[st].append((ed, t))

def djakstra(start):
    global n
    distance = [INF] * (n+1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    if start == x:
        return distance
    else:
        return distance[x]
answer = []
for i in range(n+1):
    answer.append(djakstra(i))
for i in range(len(answer[x])):
    if i != x:
        answer[i] += answer[x][i]
max_v = 0
for i in range(1, n+1):
    if i != x:
        if max_v < answer[i]:
            max_v = answer[i]
print(max_v)