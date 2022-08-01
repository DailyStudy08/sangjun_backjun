import sys
sys.stdin = open('input.txt','r')
cnt = 1
while True:
    # 여학생 수
    girl = int(input())
    # 종료 조건
    if girl == 0:
        break
    # 여학생 리스트
    girl_lst = []
    # 압수 체크 번호
    apsu = []
    # 압수 명단
    apsu_lst = []

    for _ in range(girl):
        girl_lst.append(input())
    
    for _ in range(girl*2 - 1):
        a, b = input().split()
        if a in apsu:
            apsu.remove(a)
            apsu_lst.remove(girl_lst[int(a)-1])
        else:
            apsu.append(a)
            apsu_lst.append(girl_lst[int(a)-1])
    print(f'{cnt} {apsu_lst[0]}')
    cnt += 1