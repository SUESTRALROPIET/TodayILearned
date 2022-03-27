def solution(relation):
    answer = 0

    N = len(relation)       # 사람 수 
    M = len(relation[0])    # 조건 수 
    answer_lst = []         # 후보키 리스트

    stack = [[i] for i in range(M)] # 초기 stack (인덱스 전체)

    while stack:
        idx_lst = stack.pop(0)  # idx로 적혀 있는 idx_lst
        not_minimality = False  # 최소성을 통과하는지 
    
        # 최소성 검사
        now_len = len(idx_lst)  # idx_lst 길이
        for answer_ele in answer_lst:   # 후보키 리스트 끝까지 반복하면서
            sum_lst = set(answer_ele + idx_lst) # idx_lst + 후보키 한 후, set형태로 변환
            if now_len >= len(sum_lst): # set 길이가 idx_lst길이보다 작으면 => 최소성 검사 통과 X
                not_minimality = True       ## (예시) idx_lst = [1, 2, 3]
                                            ##       answer_ele = [1, 2]
                                            ##       sum_lst = {1, 2, 3}
                                                            
        if not_minimality:  # 최소성 검사 통과 못하면 다음 stack 탐색
            continue

        check_set = list()
        for rel in relation:    # 사람들 모두 반복하면서 
            rel_status = []
            for idx in idx_lst:      # 해당 idx에 대응하는 값을
                rel_status.append(rel[idx])
            check_set.append(tuple(rel_status)) # tuple형태로 check_set에 담기

        check_set = set(check_set)  # check_set을 set형태로 변환하여 
        if len(check_set) == N:         # check_set 길이가 N이면 =>  후보키
            answer_lst.append(idx_lst)
            answer += 1
        else:                           # 후보키가 아니면! 
            std = idx_lst[-1]           
            for next_idx in range(std+1, M):    # 후보키 가장 뒤 idx번호 다음부터 탐색
                nxt_lst = idx_lst + [next_idx]  # 현재 idx_lst 뒤에 next_idx 조건 추가해서 stack에 추가
                stack.append(nxt_lst)

    return answer


solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])