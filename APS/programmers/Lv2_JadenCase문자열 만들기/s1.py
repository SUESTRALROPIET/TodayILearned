def solution(s):
    answer = ''
    fst_ele = True
    
    for ele in s:
        if ele == ' ':
            fst_ele = True
            answer += ele
            continue
            
        if fst_ele:
            answer += ele.upper()
            fst_ele = False
        else:
            answer += ele.lower()
    
    return answer