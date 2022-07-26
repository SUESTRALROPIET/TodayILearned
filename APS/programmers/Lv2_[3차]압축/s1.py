def solution(msg):
    answer = []
    dic = dict()
    
    for idx in range(1, 27):
        dic[chr(idx + 64)] = idx
        
    N = len(msg)    # 문자열 길이
    start_idx = 0   # 탐색 부분 문자: 시작 인덱스
    lst_idx = 27    # dic의 마지막 idx 번호
    max_len = 1     # dic에 담긴 문자열 길이의 최대값
    
    while start_idx < N:    # start_idx: 0 > N-1
        for now_len in range(max_len, 0, -1):   # now_len: max_len > 1 (길이가 최소 1이 되도록)
            end_idx = start_idx + now_len
            now_msg = msg[start_idx : end_idx]  # 탐색할 문자열

            if now_msg not in dic:  # 없으면 길이 줄여서 재탐색
                continue
                
            answer.append(dic[now_msg]) # answer에 문자열 해당 idx 추가
            
            if end_idx < N:     # end_idx가 N보다 작으면 => 다음 문자 추가한 문자열 dic에 추가
                new_msg = msg[start_idx : end_idx + 1]
                dic[new_msg] = lst_idx
                lst_idx += 1

                M = len(new_msg)    # max_len 갱신
                if max_len < M:
                    max_len = M
                    
            start_idx += now_len    # 탐색 및 dic에 추가 완료되면 다음 start_idx 탐색
            break
            
    return answer