def solution(priorities, location):
    answer = 0
    
    tuple_lst = []
    
    for idx, value in enumerate(priorities):
        tuple_lst.append((value, idx))
    
    while tuple_lst:
        value, idx = tuple_lst.pop(0)
        
        if tuple_lst:
            max_num = max(tuple_lst)
        else:
            max_num = (value, idx)
            
        if value < max_num[0]:
              tuple_lst.append((value, idx))
        else:
            answer += 1
            if idx == location:
                break

    return answer