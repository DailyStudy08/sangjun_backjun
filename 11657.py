import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
nodes = []
inf = 1e9
dist = [inf] * (n+1)
dist[1] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    nodes.append((a, b, c))
def bellman_ford():
    for i in range(n):
        for a, b, c in nodes:
            if dist[a] != inf and dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                if i == n - 1:
                    return False
    return True
if bellman_ford():
    for i in range(2, n+1):
        if dist[i] == inf:
            print(-1)
        else:
            print(dist[i])
else:
    print(-1)