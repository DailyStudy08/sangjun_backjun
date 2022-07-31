
n = int(input())

for i in range(n):
    A = list(map(int, input().split()))
    avg = sum(A[1:])/A[0]
    cnt = 0
    for k in A[1:]:
        if k > avg:
            cnt += 1
    rate = cnt/A[0] * 100
    print(f'{rate:.3f}%')