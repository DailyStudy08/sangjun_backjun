y, x = map(int, input().split())
arr = []
cntx = 0
cnty = 0
for i in range(y):
    arr.append(list(input()))

for i in range(y):
    temp = False
    for j in range(x):
        if arr[i][j] == 'X':
            temp = True
    if not temp:
        cntx += 1

for i in range(x):
    temp = False
    for j in range(y):
        if arr[j][i] == 'X':
            temp = True
    if not temp:
        cnty += 1
print(max(cntx, cnty))