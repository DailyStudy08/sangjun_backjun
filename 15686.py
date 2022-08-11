import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
# 세로줄과 최대 닭집
row, chicken = map(int, input().split())
# 고객 좌표와 닭집 좌표를 저장(순차로 저장됨)
lst_1 = []
lst_2 = []
for i in range(row):
    a = list(map(int, input().split()))
    for j in range(row):
        if a[j] == 1:
            lst_1.append((i, j))
        elif a[j] == 2:
            lst_2.append((i, j))
l1 = len(lst_1)
l2 = len(lst_2)
# 닭집의 조합을 만들어 내자 (튜플, 셋 이런거 쓰면 시간초과...)
can_chicken = list()
visit = [False] * l2
s = list()
def df():
    if len(s) == chicken:
        can_chicken.append(s[:])
        return
    else:
        for i in range(l2):
            if visit[i] == True:
                continue
            # 중복 제거
            if s and s[-1] > lst_2[i]:
                continue
            s.append(lst_2[i])
            visit[i] = True
            df()
            s.pop()
            visit[i] = False
df()
# 닭집의 최소거리를 재야함
cnt = 100000000
for i in can_chicken:
    # 각 고객 집까지의 최소거리
    result = [100000000] * l1
    for j in i:
        for k in range(l1):
            x = abs(j[0] - lst_1[k][0]) + abs(j[1] - lst_1[k][1])
            if result[k] > x:
                result[k] = x
    n = sum(result)
    if n < cnt:
        cnt = n
print(cnt)