import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


n = input().strip()
check = input().strip()
stack_str = []
for i in range(len(n)):
    stack_str.append(n[i])
    if len(stack_str) > len(check)-1 and stack_str[-1] == check[-1]:
        for j in range(len(check)):
            if stack_str[-len(check)+j] != check[j]:
                break
        else:
            for _ in range(len(check)):
                stack_str.pop()
print("".join(stack_str) if stack_str else "FRULA")