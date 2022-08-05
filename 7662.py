import sys
import heapq
sys.stdin = open('input.txt', 'r')

t = int(input())

for _ in range(t):
    # 순서를 기록해주기
    visited = [False] * 1000001
    q = int(input())
    min_heap = []
    max_heap = []
    for i in range(q):
        s, n = input().split()
        if s == "I":
            # 힙에 집어넣고 순서기록
            heapq.heappush(min_heap, (int(n), i))
            heapq.heappush(max_heap, (-int(n), i))
            visited[i] = True
        else:
            if n == '-1':
                # 만약에 힙에 있고 맥스에서 방문을 했다면 빼주기
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                # 힙이 비지 않았다면 방문 처리해주고 빼주기
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            else:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')