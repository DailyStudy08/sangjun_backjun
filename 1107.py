import sys
sys.stdin = open('input.txt', 'r')

channel = int(input())
no_button = int(input())
if no_button != 0:
    button_lst = set(input().split())
else:
    button_lst = set([])

result = []
for i in range(0, 1000000):
    if not set(list(str(i))) & set(button_lst):
        result.append(i)

mini_result = 999999
mini_number = 0
for j in result:
    if mini_result > abs(channel - j):
        mini_result = abs(channel - j)
        mini_number = j

if abs(100 - channel) > mini_result + len(str(mini_number)):
    print(mini_result + len(str(mini_number)))
else:
    print(abs(100 - channel))