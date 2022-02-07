def solution(scoville, K):
    answer = 0
    
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
        answer += 1
        fst = scoville.pop(0)
        scd = scoville.pop(0)
        new_food = fst + (scd * 2)
        scoville.append(new_food)
        scoville.sort()  
    
    return answer