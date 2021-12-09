import sys
sys.stdin = open('input.txt')

def get_boolean(row_idx, col_idx, now_status):
    
    di = [0, 2, 0, -2]  # 우 / 하 / 좌 / 상 으로 row_idx/col_idx와의 길이가 2인 부분 탐색하기
    dj = [2, 0, -2, 0]

    for k in range(4):
        ni = row_idx + di[k]
        nj = col_idx + dj[k]
        if (0 <= ni < M and 0 <= nj < N) and matrix[ni][nj] == '#':
            matrix[ni][nj] = not now_status
            get_boolean(ni, nj, not now_status)
            
T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [['#'] * N for _ in range(M)]

    for row in range(M):
        for col in range(N):
            if matrix[row][col] == '#':
                matrix[row][col] = True
                get_boolean(row, col, True)


    result = 0
    for row in range(M):
        result += sum(matrix[row])

    print('#{} {}'.format(test, result))