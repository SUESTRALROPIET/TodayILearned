import sys
sys.stdin = open('input.txt')

def dfs(now_x, now_y, cnt):
    visited[now_x][now_y] = 1

    di = [-1, -1, -1, 0, 1, 1, 1, 0]
    dj = [-1, 0, 1, 1, 1, 0, -1, -1]

    now_cnt = 0
    for k in range(8):
        ni = now_x + di[k]
        nj = now_y + dj[k]
        if not (0 <= ni < N and 0 <= nj < N):
            continue
        if visited[ni][nj] or matrix[ni][nj] == '.':
            continue
        if matrix[ni][nj] == '*':
            now_cnt += 1

    matrix[now_x][now_y] = now_cnt
    if matrix[now_x][now_y] == 0:
        for k in range(8):
            ni = now_x + di[k]
            nj = now_y + dj[k]
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if visited[ni][nj]:
                continue
            dfs(ni, nj, cnt+1)

T = int(input())
for test in range(1, 2):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '.':
                dfs(i, j, 1)

    print(matrix)