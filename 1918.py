n = input()
stack = []
result = []
prior = {'*':3,'/':3,'+':2,'-':2,'(':1} 
for i in n:
    if stack:
        if i in '()':
            if i == '(':
                stack.append(i)
            else:
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
        elif i in '+-*/':
            while stack and prior[i] <= prior[stack[-1]]:
                result.append(stack.pop())
            stack.append(i)
        else:
            result.append(i)
    else:
        if i in '()+-*/':
            stack.append(i)
        else:
            result.append(i)
    print(stack)
while stack:
    result.append(stack.pop())
print(''.join(result))