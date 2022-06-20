def solution(number, k):
    answer = ''
    
    chgNum = list(map(int, number))
    numLen = len(number)
    std = round(sum(chgNum) / numLen)
    
    for idx in range(numLen):
        if chgNum[idx] <= std:
            k -= 1
        else:
            answer += str(chgNum[idx])
        if not k:
            j = list(map(str, chgNum[idx+1:]))
            l = ''.join(j)
            answer += l
            break
            
    return answer