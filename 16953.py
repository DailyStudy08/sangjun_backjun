a, b = map(int, input().split())
cnt = 1
while b > a:
    if b%10 == 1:
        b = (b-1)/10
    elif b % 2 == 0:
        b /= 2
    else:
        break
    cnt += 1
print(cnt if b == a else -1)