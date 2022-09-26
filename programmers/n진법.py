def solution(n, t, m, p):
    over = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    answer = ''
    for i in range(10):
        over[i] = str(i)
    arr = []
    j = 0
    while len(arr) <= t*m:
        i = j
        if i == 0:
            arr.append('0')
        else:
            num = ''
            while i > 0:
                num = over[i%n] + num
                i //= n
            arr.extend(list(num))
        j += 1
    for i in range(p-1, t*m, m):
        answer += arr[i]
    return answer