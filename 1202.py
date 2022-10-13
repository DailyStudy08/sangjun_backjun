import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

import heapq

n, k = map(int, input().split())
q = []
q_bag = []
bag_possible = []
ans = 0
for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(q, (m, v))
for j in range(k):
    c = int(input())
    q_bag.append(c)
q_bag.sort()

for i in q_bag:
    while q and i >= q[0][0]:
        heapq.heappush(bag_possible, -heapq.heappop(q)[1])
    if bag_possible:
        ans -= heapq.heappop(bag_possible)
    elif not q:
        break
# while q:
#     m, v = heapq.heappop(q)
#     if m <= q_bag[-1]:
#         heapq.heappush(bag_possible, (-v, m))
# while bag_possible:
#     v, m = heapq.heappop(bag_possible)
#     for i in range(len(q_bag)):
#         if q_bag[i] >= m:
#             ans -= v
#             q_bag.pop(i)
#             break
print(ans)