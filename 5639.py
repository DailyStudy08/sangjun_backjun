import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

post = []
while True:
    try:
        post.append(int(input()))
    except:
        break

def posttorear(first, end):
    # 재귀탈출조건
    if first > end:
        return
    # 리스트로 나눴을때 마지막까지 포함될 수 있게
    mid = end+1
    for i in range(first+1, end+1):
        # 이진트리니까 더 큰게 있으면 오른쪽 노드
        if post[first] < post[i]:
            mid = i
            break
    # 왼쪽노드도 똑같이 실행
    posttorear(first+1, mid-1)
    # 오른쪽 노드도 똑같이 실행
    posttorear(mid, end)
    # 부모노드는 제일 마지막에 출력해줌
    print(post[first])
    
posttorear(0, len(post)-1)