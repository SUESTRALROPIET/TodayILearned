import sys
sys.stdin = open('input.txt')

def dfs(now_x, now_y):
    # 방문체크
    visited[now_x][now_y] = 1
    # 8 방향
    di = [-1, -1, -1, 0, 1, 1, 1, 0]
    dj = [-1, 0, 1, 1, 1, 0, -1, -1]
    # 주변 지뢰 개수 세기
    bomb_cnt = 0
    for k in range(8):
        ni = now_x + di[k]
        nj = now_y + dj[k]
        if not (0 <= ni < N and 0 <= nj < N):   # 유효성 검사
            continue
        if visited[ni][nj] or matrix[ni][nj] == '.':    # 방문한 적이 있거나 지뢰가 없으면 continue
            continue
        if matrix[ni][nj] == '*':   # 지뢰면 지뢰개수 세기
            bomb_cnt += 1
    # 지뢰 개수 담기
    temp_matrix[now_x][now_y] = bomb_cnt

    # 담긴 지뢰 개수가 0이면 주변 연쇄적으로 터뜨리기
    if temp_matrix[now_x][now_y] == 0:
        for k in range(8):
            ni = now_x + di[k]
            nj = now_y + dj[k]
            # 유효성 검사
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            # 방문한 적 있으면 continue
            if visited[ni][nj]:
                continue
            dfs(ni, nj)

T = int(input())
for test in range(1, T+1):
    # 지뢰 맵 초기화
    N = int(input())
    matrix = [list(input()) for _ in range(N)]

    temp_matrix = [['*'] * N for _ in range(N)]

    # 방문 체크
    visited = [[0] * N for _ in range(N)]

    result_cnt = 0

    # (0, 0) 부터 체크 
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '.':
                dfs(i, j)

    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            if matrix[i][j] == '*':
                continue
            if temp_matrix[i][j] == 0:
                result_cnt += 1
                dfs(i, j)
            else:
                di = [-1, -1, -1, 0, 1, 1, 1, 0]
                dj = [-1, 0, 1, 1, 1, 0, -1, -1]
                for k in range(8):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if not (0 <= ni < N and 0 <= nj < N):
                        continue
                    if temp_matrix[ni][nj] == 0:
                        result_cnt += 1
                        dfs(ni, nj)
            
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            if matrix[i][j] == '*':
                continue
            result_cnt += 1
            dfs(i, j)

    print('#{} {}'.format(test, result_cnt))