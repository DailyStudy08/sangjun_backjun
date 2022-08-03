from itertools import combinations

result = []
for _ in range(9):
    result.append(int(input()))

answer_lst = list(combinations(result, 7))
answer = []
for i in answer_lst:
    if sum(i) == 100:
        answer = i
for i in sorted(answer):
    print(i)