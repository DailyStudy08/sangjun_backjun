from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# n, m = map(int, input().split())
# nt, *true = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# party = []
# for _ in range(m):
#     p, *people = map(int, input().split())
#     if p != 1:
#         for i in people:
#             for j in people:
#                 if i != j:
#                     graph[i].append(j)
#     party.append(people)
# def bfs(li):
#     visited = [0] * (n+1)
#     queue = deque(li)
#     while queue:
#         q = queue.popleft()
#         visited[q] = 1
#         if q in true:
#             return 0
#         for i in graph[q]:
#             if visited[i] == 0:
#                 queue.append(i)
#     return 1
# cnt = 0
# for i in party:
#     cnt += bfs(i)
# print(cnt)

n, m = map(int, input().split())
truth = [i for i in range(n+1)]
true_p = list(map(int, input().split()))[1:]
for i in true_p:
    truth[i] = 0
def find(x):
    if truth[x] != x:
        # 재귀로 구현
        truth[x] = find(truth[x])
    return truth[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        truth[b] = a
    else:
        truth[a] = b
        
parties = []
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    for i in range(len(party)-1):
        union(party[i], party[i+1])
    parties.append(party)

answer = 0
for party in parties:
    know = False
    for i in range(len(party)):
        if find(party[i]) == 0:
            know = True
            break
    if not know:
        answer += 1
        
print(answer)