import sys
sys.stdin = open('input.txt')

def get_boolean(row_idx, col_idx, now_status):
                    # row_idx / col_idx 기준
    di = [0, 2, 2]  # 우측 2칸 / 우측 2칸 + 아래 2칸 / 아래 2칸
    dj = [2, 2, 0]

    for k in range(3):
        ni = row_idx + di[k]
        nj = col_idx + dj[k]
        if (0 <= ni < M and 0 <= nj < N) and matrix[ni][nj] == '#':
            matrix[ni][nj] = not now_status     # True/False 번갈아 담기
            get_boolean(ni, nj, not now_status) # DFS 탐색
            
T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [['#'] * N for _ in range(M)]

    for row in range(M):
        for col in range(N):
            if matrix[row][col] == '#':     # 아직 탐색하지 않은 곳을 
                matrix[row][col] = True         # True값으로 담고
                get_boolean(row, col, True)         # DFS 출발하기


    result = 0
    for row in range(M):        # True값이 담긴 원소들 합연산으로 결과값 반환하기
        result += sum(matrix[row])  

    print('#{} {}'.format(test, result))