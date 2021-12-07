import sys
sys.stdin = open('input.txt')

def get_result(row_idx, col_idx, result_len, cur_str):

    if result_len == 7:     # 문자열이 7자리가 되면 함수 종료
        if not (cur_str in possible_str):   # possible_str에 담긴 문자열이 아니면 추가 
            possible_str.append(cur_str)
        return 
    
    di = [0, 1, 0, -1]  # 델타이동: 우 / 하 / 좌 / 상
    dj = [1, 0, -1, 0]

    for k in range(4):
        ni = row_idx + di[k]
        nj = col_idx + dj[k]
        
        if not (0 <= ni < 4 and 0 <= nj < 4):   # 유효성 검사
            continue

        get_result(ni, nj, result_len + 1, cur_str + matrix[ni][nj])    # 7자리가 될때까지 dfs 탐색

    

T = int(input())
for test in range(1, T+1):
    matrix = [list(input().split()) for _ in range(4)]  # 4 X 4 행렬

    possible_str = []                   # 7자리 숫자 담기 

    for row in range(4):                # 모든 위치에서 출발하기 (row index, col index, 문자열 길이, 현재 문자열)
        for col in range(4):
            get_result(row, col, 1, matrix[row][col])

    print('#{} {}'.format(test, len(possible_str)))
