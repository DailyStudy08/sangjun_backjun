import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def find_p(x):
    if x != parents[x]:
        parents[x] = find_p(parents[x])
    return parents[x]

def union_p(a, b):
    a = find_p(a)
    b = find_p(b)
    if a != b:
        parents[b] = a
        friends[a] += friends[b]
        
n = int(input())
for _ in range(n):
    m = int(input())
    parents = dict()
    friends = dict()
    for _ in range(m):
        a, b = input().strip().split()
        if not a in parents:
            parents[a] = a
            friends[a] = 1
        if not b in parents:
            parents[b] = b
            friends[b] = 1
        if find_p(a) != find_p(b):
            union_p(a, b)
        print(friends[find_p(a)])