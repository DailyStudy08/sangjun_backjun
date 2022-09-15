S = input()
T = input()
temp = False
def ab(n):
    global temp
    if len(n) < len(S):
        return
    if n == S:
        temp = True
        return
    if temp == True:
        return
    if n[-1] == 'A':
        ab(n[:-1])
    if n[0] == 'B':
        m = n[1:]
        m = m[::-1]
        ab(m)
ab(T)
print(int(temp))