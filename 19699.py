n, m = map(int, input().split())
arr = list(map(int, input().split()))
visit = [0 for _ in range(len(arr))]
answer = set()
def isPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def back(start,depth,sum_cow):
    if depth==m:
        if isPrime(sum_cow):
            answer.add(sum_cow)
    for i in range(start,n):
        if not visit[i]:
            visit[i]=True
            back(i+1,depth+1,sum_cow+arr[i])
            visit[i]=False
back(0, 0, 0)
answer = list(answer)
answer.sort()
if answer:
    print(*answer)
else:
    print(-1)