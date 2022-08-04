import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
# 그래프 생성
ladder = [[0,1000] for _ in range(101)]
# 사다리 뱀 정해주기
bridge, snake = map(int, input().split())

for _ in range(bridge+snake):
    start, end = map(int, input().split())
    ladder[start][0] = end
    
# 방문처리하면서 몇번째 방문했는지
def snake(start):
    queue = deque()
    queue.append((start,0))
    while queue:
        v,cnt = queue.popleft()
        if v == 100:
          return cnt
        # 1 >> 2,3,4,5,6,7
        for i in range(v+1,v+7):
            if i <=100 and ladder[i][1] > cnt:
              if ladder[i][0] > 0:
                queue.append((ladder[i][0],cnt+1))
              else:
                queue.append((i,cnt+1))
              ladder[i][1] = cnt
         
print(snake(1))



# from collections import deque
# # 그래프 생성
# graph = [[] for _ in range(101)]
# for i in range(1,101):
#     for j in range(1,7):
#         if i+j <=100:
#             # 어디서 출발하고 어디로 가는지
#             graph[i].append((i+j, i))
# # 사다리 뱀 정해주기
# bridge, snake = map(int, input().split())
# snake_lst = []
# for _ in range(bridge+snake):
#     start, end = map(int, input().split())
#     graph[start].append((end, start))
#     snake_lst.append((end, start))
# # 방문처리하면서 몇번째로 방문했는지
# visited = [-1 for _ in range(101)]

# def snake(start):
#     queue = deque([graph[start]])
#     visited[start] = 0
#     while queue:
#         v = queue.popleft()
#         for i in v:
#             a, b = i
#             if visited[a] == -1:
#                 visited[a] = visited[b] + 1
#                 if i in snake_lst:
#                     visited[a] -= 1
#                 queue.append(graph[a])
# snake(1)
# print(visited[100])

# # 플로이드 워셜 22% 틀렸습니다
# from math import inf
# # 기본그래프
# graph = [[inf for _ in range(100)]for _ in range(100)]
# for i in range(100):
#     for j in range(100):
#         if i == j:
#             graph[i][j] = 0
#         if i < j <= i+6:
#             graph[i][j] = 1

# bridge, snake = map(int, input().split())
# for _ in range(bridge+snake):
#     start, end = map(int, input().split())
#     graph[start-1][end-1] = 0

# for i in range(100):
#     for j in range(100):
#         for k in range(100):
#             graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

# print(graph[0])