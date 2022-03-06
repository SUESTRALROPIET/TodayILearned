def solution(priorities, location):
    answer = 0  # 프린트되는 횟수
    
    tuple_lst = []  # (원소값, 기존 idx번호) tuple 형태로 묶어서 담기
                    #   => max값 구할 때 원소값 기준으로 찾기 위해서  
    for idx, value in enumerate(priorities):
        tuple_lst.append((value, idx))
    
    while tuple_lst:    # tuple_lst 하나씩 팝업하면서 탐색
        value, idx = tuple_lst.pop(0)
        
        # 최대값 찾기
        if tuple_lst:   # tuple_lst 최대값 찾기
            max_num = max(tuple_lst)
        else:           # tuple_lst 원소를 모두 pop해서 아무것도 없을 때
            max_num = (value, idx)
            
        if value < max_num[0]:  # 현째 pop한 원소가 max값이 아니면
              tuple_lst.append((value, idx))    # 다시 tuple_lst 끝에 붙이기
        else:                   # max값이면
            answer += 1         # 프린트 횟수 추가
            if idx == location: # 현재 idx가 location과 같다면 반복문 끝내기
                break

    return answer