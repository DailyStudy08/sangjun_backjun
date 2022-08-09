import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
result = set()
def tetro(y, x) :
    t, b, l, r, bb, rr, tl, tr, bl, br = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    me = arr[y][x]
    if 0<= y-1 < n:
        t = arr[y-1][x]
    if 0<= y+1 < n:
        b = arr[y+1][x]
    if 0<= x-1 < m:
        l = arr[y][x-1]
    if 0<= x+1 < m:
        r =arr[y][x+1]
    if 0<= y+2 < n:
        bb = arr[y+2][x]
    if 0<= x+2 < m:
        rr = arr[y][x+2]
    if 0 <= y-1 < n and 0 <= x-1 < m:
        tl = arr[y-1][x-1]
    if 0 <= y-1 < n and 0 <= x+1 < m:
        tr = arr[y-1][x+1]
    if 0 <= y+1 < n and 0 <= x-1 < m:
        bl = arr[y+1][x-1]
    if 0 <= y+1 < n and 0 <= x+1 < m:
        br = arr[y+1][x+1]
    if l and r and rr:
        result.add(l+me+r+rr)
    if t and b and bb:
        result.add(t+b+bb+me)
    if r and b and br:
        result.add(r+b+br+me)
    if t and b and bl:
        result.add(t+b+bl+me)
    if t and b and br:
        result.add(t+b+br+me)
    if l and r and tr:
        result.add(tr+l+r+me)
    if l and r and tl:
        result.add(l+r+tl+me)
    if t and b and tl:
        result.add(t+b+tl+me)
    if t and b and tr:
        result.add(t+b+tr+me)
    if l and r and bl:
        result.add(l+r+bl+me)
    if l and r and br:
        result.add(l+r+br+me)
    if t and r and br:
        result.add(t+r+br+me)
    if t and r and br:
        result.add(t+l+bl+me)
    if r and b and bl:
        result.add(r+b+bl+me)
    if l and b and br:
        result.add(l+b+br+me)
    if l and b and t:
        result.add(l+b+t+me)
    if r and b and t:
        result.add(r+b+t+me)
    if l and b and r:
        result.add(l+r+b+me)
    if l and t and r:
        result.add(l+t+r+me)
for i in range(n):
    for j in range(m):
        tetro(i, j)
print(max(result))