from collections import deque

expression = "100-200*300-500+20"

def combi(x, n):
    if n == 3:
        combi_dict.append(cd[:])
        return
    for i in range(3):
        if pmd_v[i] != 0:
            continue
        pmd_v[i] = 1
        cd.append(i)
        combi(x, n+1)
        pmd_v[i] = 0
        cd.pop()
    

def solution(expression):
    global pmd, cd, pmd_v, combi_dict
    pmd = ['+', '-', '*']
    pmd_v = [0, 0, 0]
    cd = []
    combi_dict = []
    combi(pmd, 0)
    p_dict = dict()
    stack = deque()
    ex = []
    ans = 0
    s = ''
    for i in range(len(expression)):
        if expression[i] in "+-*":
            ex.append(int(s))
            s = ''
            ex.append(expression[i])
        elif len(expression) - 1 == i:
            s += expression[i]
            ex.append(int(s))
        else:
            s += expression[i]
    for i in combi_dict:
        for j in range(3):
            p_dict[pmd[j]] = i[j]
        if combi_dict == {'+': 1, '-': 0, '*': 2}:
            pass
        for k in range(len(ex)):
            if len(stack) < 3:
                stack.append(ex[k])
            else:
                if type(ex[k]) == int:
                    stack.append(ex[k])
                else:
                    if p_dict[stack[-2]] <= p_dict[ex[k]]:
                        stack.append(ex[k])
                    else:
                        num2 = stack.pop()
                        pm = stack.pop()
                        num1 = stack.pop()
                        if pm == '+':
                            stack.append(num1+num2)
                        elif pm == '-':
                            stack.append(num1-num2)
                        else:
                            stack.append(num1*num2)
                        stack.append(ex[k])
        if combi_dict == {'+': 1, '-': 0, '*': 2}:
            pass
        while len(stack) > 1:
            if len(stack) >= 4:
                if p_dict[stack[1]] < p_dict[stack[3]]:   
                    num1 = stack.pop()
                    pm = stack.pop()
                    num2 = stack.pop()
                    if pm == '+':
                        stack.append(num1+num2)
                    elif pm == '-':
                        stack.append(num1-num2)
                    else:
                        stack.append(num1*num2)
                else:
                    num1 = stack.popleft()
                    pm = stack.popleft()
                    num2 = stack.popleft()
                    if pm == '+':
                        stack.appendleft(num1+num2)
                    elif pm == '-':
                        stack.appendleft(num1-num2)
                    else:
                        stack.appendleft(num1*num2)
            else:
                num1 = stack.popleft()
                pm = stack.popleft()
                num2 = stack.popleft()
                if pm == '+':
                    stack.appendleft(num1+num2)
                elif pm == '-':
                    stack.appendleft(num1-num2)
                else:
                    stack.appendleft(num1*num2)
        if ans < abs(stack[-1]):
            ans = abs(stack[-1])
        stack = deque()
    return ans

print(solution(expression))