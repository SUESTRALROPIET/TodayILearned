def solution(places):
    answer = []
    def is_safe(place_table):
        for i in range(5):
            for j in range(5):
                if place_table[i][j] == 'P':
                    if not check_around(place_table, 'P', i, j):    # P 없으면 됨
                        return 0
                elif place_table[i][j] == 'O':
                    if not check_around(place_table, 'O', i, j):    # P가 하나 이하로 있으면 됨
                        return 0   
        return 1
                    
    def check_around(place, now_chr, row, col):
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]
        p_cnt = 0
        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if not(0 <= ni < 5 and 0 <= nj < 5):
               continue
            if place[ni][nj] == 'P':
                p_cnt += 1
        
        if now_chr == 'P':
            if p_cnt:
                return False
            else:
                return True
        if now_chr == 'O':
            if p_cnt <= 1:
                return True
            else:
                return False
            
    for place in places:
        answer.append(is_safe(place))
    
    return answer