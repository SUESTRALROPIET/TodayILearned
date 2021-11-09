import sys
sys.stdin = open('input.txt')

def dfs(start_i, start_j, now_i, now_j, cnt):
    global result_num, result_cnt

    if result_cnt <= cnt:
        if result_cnt == cnt and matrix[start_i][start_j] < result_num:
            result_num = matrix[start_i][start_j]
        else:
            result_num = matrix[start_i][start_j]
            result_cnt = cnt

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for k in range(4):
        ni = now_i + di[k]
        nj = now_j + dj[k]
        if not (0 <= ni < N and 0 <= nj < N):
            continue
        if matrix[now_i][now_j] + 1 == matrix[ni][nj]:
            dfs(start_i, start_j, ni, nj, cnt+1)

T = int(input())
for test in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result_num = 0
    result_cnt = 0

    for i in range(N):
        for j in range(N):
            dfs(i, j, i, j, 1)

    print('#{} {} {}'.format(test, result_num, result_cnt))
