import sys
sys.stdin = open('input.txt')
from cmath import inf
import heapq
input = sys.stdin.readline

city = int(input())
node = int(input())

graph = [[]for _ in range(city+1)]
distance = [inf] * (city+1)
visit = [False] * (city+1)

for _ in range(node):
    st, ed ,v = map(int, input().split())
    graph[st].append((ed, v))

def djikstra(start):
    q = []
    distance[start] = 0
    # 시작부분 담아주기
    heapq.heappush(q, (0, start))
    while q:
        # 가는 밸류, 지금 어디서 출발하는지
        value, now = heapq.heappop(q)
        # 지금 가는거보다 밸류가 크면 판단할 가치가 없다.
        if distance[now] < value:
            continue
        # 갈 수 있는 간선 불러오기
        for i in graph[now]:
            # 비용은 일단 지금 불러온데에다가 간선밸류 더해준 값
            cost = value + i[1]
            # 이 비용이 기존에 간선비용보다 작으면 넣어줘야지
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 작으면 가능성 있으니까 힙에 넣어주기
                heapq.heappush(q, (cost, i[0]))

start, end = map(int, input().split())
djikstra(start)
print(distance[end])