from collections import deque

def solution(queue1, queue2):
    answer = 0

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    while sum1 != sum2:
        if not (queue1 and queue2):
            answer = -1
            break
        if sum1 < sum2:
            pop_ele = deque.popleft(queue2)
            sum2 -= pop_ele
            sum1 += pop_ele
            deque.append(queue1, pop_ele)
            answer += 1
        elif sum1 > sum2:
            pop_ele = deque.popleft(queue1)
            sum1 -= pop_ele
            sum2 += pop_ele  
            deque.append(queue2, pop_ele)
            answer += 1
            
    return answer