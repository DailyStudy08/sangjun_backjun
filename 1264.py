while True:
    a = input()
    if a == '#':
        break
    cnt = 0
    for i in range(len(a)):
        if a[i].lower() in 'aeiou':
            cnt += 1
    print(cnt)