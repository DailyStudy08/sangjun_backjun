import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
tc = int(input())
inf = 1e9
for t in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    # 모든 간선의 길이를 무한대로 설정
    dist = [inf]*(n+1)
    # n-1번째의 길이를 저장할 리스트
    dist_n = []
    # 출발 지점을 0으로 설정
    dist[1] = 0
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s,e,-t))

    def bellman_ford():
        for i in range(n):
            for s, e, t in edges:
                # 거쳐간 노드의 방문거리가 보다 짧으면 짧은 길이로 바꿔줌
                if dist[e] > dist[s] + t:
                    dist[e] = dist[s] + t
            print(dist)
            # 만약 과정을 한번 더 반복했을때 보다 작아진다면 음수 간선 순환이 존재
            if i == n-2:
                dist_n = dist[:]
                
            if i == n-1:
                for i in range(len(dist)):
                    if dist[i] != dist_n[i]:
                        return True
        return False
    if bellman_ford():
        print('YES')
    else:
        print('NO')