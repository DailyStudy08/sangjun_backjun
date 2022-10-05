import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def find_p(x):
    if x != parent[x]:
        parent[x] = find_p(parent[x])
    return parent[x]
# 격납고 수
g = int(input())
# 비행기 수
p = int(input())
# 격납고(부모)
parent = [i for i in range(g+1)]
cnt = 0
for _ in range(p):
    a = int(input())
    b = find_p(a)
    # 들어갈 수 있는 곳이 있다면 거기서 부모를 자신보다 1 작은 값으로 갱신
    if a >= b:
        parent[b] = b-1
    # 0번째가 -1이면 들어갈수있는 격납고가 없다는것
    if parent[0] == -1:
        break
    # 들어가는 비행기 +1
    cnt += 1
print(parent)
print(cnt)