def solution(places):
    answer = []
    def is_safe(place_table):   # 안전하면 1, 안전하지 않으면 0 반환
        for i in range(5):          # 배열을 탐색하면서
            for j in range(5):
                if place_table[i][j] == 'P':        # 원소가 P이면 주변 체크(P가 있으면 안됨)
                    if not check_around(place_table, 'P', i, j):
                        return 0
                elif place_table[i][j] == 'O':      # 원소가 O이면 주변 체크(P가 하나 이하로 있으면 됨)
                    if not check_around(place_table, 'O', i, j):
                        return 0   
        return 1                                    # 위 검사를 모두 통과하면 1 반환 (안전)
                    
    def check_around(place, now_chr, row, col):
        # 4방향 탐색 (상 / 우 / 하 / 좌)
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]

        p_cnt = 0       # 주변 탐색 시, P 개수 세기

        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if not(0 <= ni < 5 and 0 <= nj < 5):    # 범위 유효성 검사
               continue
            if place[ni][nj] == 'P':    # 주변에 P가 있으면, p_cnt 값 1씩 더하기
                p_cnt += 1

        # 모든 탐색이 끝나고
        if now_chr == 'P':  # P인 원소 주변에
            if p_cnt:           # P가 있으면 False 반환
                return False
            else:
                return True
        if now_chr == 'O':  # O인 원소 주변에
            if p_cnt <= 1:      # P가 1 이하이면 True 반환
                return True
            else:
                return False
            
    for place in places:    # 입력받은 대기실 5개 모두 탐색
        answer.append(is_safe(place))
    
    return answer