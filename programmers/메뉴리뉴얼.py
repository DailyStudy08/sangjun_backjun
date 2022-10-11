orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
def solution(orders, course):
    global new_course, menu
    answer = []
    new_course = dict()
    for i in range(len(orders)):
        arr = list(orders[i])
        arr.sort()
        orders[i] = ''.join(arr)
    for i in orders:
        menu = ''
        sub(i, 0, course)
    for i in course:
        max_v = 2
        arr = []
        for j in new_course:
            if len(j) == i and new_course[j] > max_v:
                max_v = new_course[j]
                arr = [j]
            elif len(j) == i and new_course[j] == max_v:
                arr.append(j)
        answer.extend(arr)
    return sorted(answer)

def sub(ord, n, course):
    global menu
    if n == 11:
        return
    for j in range(n, len(ord)):
        menu += ord[j]
        if len(menu) in course:
            if menu in new_course:
                new_course[menu] += 1
            else:
                new_course[menu] = 1
        sub(ord, j+1, course)
        menu = menu[:-1]

print(solution(orders, course))