import sys
sys.stdin = open('input.txt')

def dfs(now_x, now_y, result):
    global min_result
    
    if now_x == now_y == N-1:
        if result < min_result:
            min_result = result
        return

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for k in range(4):
        ni = now_x + di[k]
        nj = now_y + dj[k]

        if not (0 <= ni < N and 0 <= nj < N):
            continue

        if checked[ni][nj]:
            continue
        
        if result + matrix[ni][nj] < min_result:
            checked[ni][nj] = 1
            dfs(ni, nj, result + matrix[ni][nj])
            checked[ni][nj] = 0

T = int(input())
for test in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    checked = [[0] * N for _ in range(N)]

    checked[0][0] = 1
    min_result = float('INF')
    dfs(0, 0, 0)

    print('#{} {}'.format(test, min_result))