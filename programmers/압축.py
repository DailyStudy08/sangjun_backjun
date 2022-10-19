msg = 'TOBEORNOTTOBEORTOBEORNOT'

def solution(msg):
    answer = []
    alpha_dict = dict()
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(1, len(alp)+1):
        alpha_dict[alp[i-1]] = i
    k = 27
    n = 0
    while n < len(msg):
        word = msg[n]
        for i in range(n+1, len(msg)):
            if word + msg[i] in alpha_dict:
                word += msg[i]
            else:
                new_word = word + msg[i]
                alpha_dict[new_word] = k
                k += 1
                break
            
        answer.append(alpha_dict[word])
        n += len(word)
    return answer
print(solution(msg))