import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
# 나머지 분배법칙...
def abc(a, n):
    if n == 1:
        return a % c
    else:
        tmp = abc(a, n//2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c
print(abc(a, b))