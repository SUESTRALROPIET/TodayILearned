def solution(queue1, queue2):
    answer = 0

    sum1 = sum(queue1)
    sum2 = sum(queue2)
        
    while sum1 != sum2:
        if not (queue1 and queue2):
            answer = -1
            break
        if sum1 < sum2:
            pop_ele = queue2.pop(0)
            sum2 -= pop_ele
            sum1 += pop_ele
            queue1.append(pop_ele)
            answer += 1
        elif sum1 > sum2:
            pop_ele = queue1.pop(0)
            sum1 -= pop_ele
            sum2 += pop_ele  
            queue2.append(pop_ele)
            answer += 1
            
    return answer