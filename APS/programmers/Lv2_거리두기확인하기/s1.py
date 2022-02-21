def solution(places):
    answer = []
    def is_safe(place_table):
        for i in range(5):
            for j in range(5):
                if place_table[i][j] == 'P':
                    if check_around(place_table, i, j):
                        return 1
                    else:
                        return 0
        return 1
                    
    def check_around(place, row, col):
        # di = [-1, 0, 1, 0]
        # dj = [0, 1, 0, -1]
        di = [-1, -1, -1, 0, 1, 1, 1, 0]
        dj = [-1, 0, 1, 1, 1, 0, -1, -1]
        for k in range(8):
            ni = row
            nj = col
            stack = []
            while abs(ni - row) + abs(nj - col) <= 1:
                ni += di[k]
                nj += dj[k]
                if not(0 <= ni < 5 and 0 <= nj < 5):
                   break
                new_status = place[ni][nj]
                if new_status == 'P':
                    if 'X' in stack:
                        continue
                    else:
                        return False   
                else:
                    stack.append(new_status)
        return True

    for place in places:
        answer.append(is_safe(place))
    
    return answer