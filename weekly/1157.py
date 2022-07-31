s = input()
alpha = list(range(97, 123))
numlist = list()
for i in alpha:
    a = s.count(chr(i))+s.count(chr(i-32))
    numlist.append(a)
x = sorted(numlist, reverse=True)[1]
y = max(numlist)
if y == x:
    print("?")
else:
    print(chr(alpha[numlist.index(max(numlist))]-32))
