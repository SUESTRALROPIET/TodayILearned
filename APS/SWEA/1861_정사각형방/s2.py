import sys
sys.stdin = open('input.txt')

def dfs(start_i, start_j, now_i, now_j, cnt):
    global result_cnt, result_list

    if result_cnt < cnt:
        result_list = []
        result_cnt = cnt
        result_list.append(matrix[start_i][start_j])
    elif result_cnt == cnt:
        result_list.append(matrix[start_i][start_j])

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

    result_cnt = 0
    result_list = []

    for i in range(N):
        for j in range(N):
            dfs(i, j, i, j, 1)

    print('#{} {} {}'.format(test, min(result_list), result_cnt))
