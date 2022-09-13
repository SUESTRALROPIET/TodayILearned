from copy import deepcopy

def solution(arr):    
    answer = 1
    answer_lst = []
    
    for num in arr:
        ele_lst = []    # num의 약수가 담김
        ele = 2
        while ele <= num + 1:
            if num % ele == 0:
                ele_lst.append(ele)
                num //= ele
            else:
                ele += 1
        
        # 다중집합 연산: 합집합 - 교집합
        temp_ele_lst = deepcopy(ele_lst)
        for ans in answer_lst:
            if ans in temp_ele_lst:
                temp_ele_lst.remove(ans)
                
        answer_lst += temp_ele_lst
        
    for ans_ele in answer_lst:
        answer *= ans_ele        
    
    return answer