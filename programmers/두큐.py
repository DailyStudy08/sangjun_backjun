def solution(queue1, queue2):
    answer = -1
    # a=sum(queue1)
    # b=sum(queue2)
    # s=(a+b)//2
    # i,j,t=0,0,len(queue1)
    # while i<2*t and j<2*t and a!=b:
    #     if a<s:
    #         a+=queue2[j]
    #         b-=queue2[j]
    #         queue1.append(queue2[j])
    #         j+=1
    #     else:
    #         a-=queue1[i]
    #         b+=queue1[i]
    #         queue2.append(queue1[i])
    #         i+=1
    # if a==s:
    #     answer=i+j
        
    sq1 = sum(queue1)
    sq2 = sum(queue2)
    result = (sq1 + sq2) // 2
    i, j, t1, t2 = 0, 0, len(queue1), len(queue2)
    while i < t1 + t2 and j < t1 + t2 and sq1 != sq2:
        if sq1 < result:
            sq1 += queue2[j]
            sq2 -= queue2[j]
            queue1.append(queue2[j])
            j += 1
        else:
            sq1 -= queue1[i]
            sq2 += queue1[i]
            queue2.append(queue1[i])
            i += 1
    if sq1 == sq2:
        answer = i+j
    return answer
    
            
queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]

print(solution(queue1, queue2))