import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    arr = list(map(int, input().split()))
    graph = [[]for _ in range(n+1)]
    degree = [0] * (n+1)
    
    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1
        
    w = int(input())
    
    answer = [0] * (n+1)
    
    def topo(w):
        build = []
        q = deque()
        next = deque()
        for i in range(1, n+1):
            if degree[i] == 0:
                answer[i] = arr[i-1]
                q.append(i)
        while q:
            node = q.popleft()
            build.append(node)
            for i in range(len(graph[node])):
                k = graph[node].pop()
                degree[k] -= 1
                answer[k] = max(answer[node] + arr[k-1], answer[k])
                if degree[k] == 0:
                    q.append(k)
                    if k == w:
                        return
            
    topo(w)
    print(answer[w])