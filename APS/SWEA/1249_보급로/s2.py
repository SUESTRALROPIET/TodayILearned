import sys
sys.stdin = open('input.txt')

def bfs():
    global min_result
    
    stack_idx = 0

    while stack_idx < len(stack):
        now_x, now_y, result = stack[stack_idx]

        if now_x == now_y == N-1:
            if result < min_result:
                min_result = result
                
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        for k in range(4):
            ni = now_x + di[k]
            nj = now_y + dj[k]

            if not (0 <= ni < N and 0 <= nj < N):
                continue

            if result + matrix[ni][nj] < min_result:
                stack.append((ni, nj, result + matrix[ni][nj]))
            
        stack_idx += 1

T = int(input())
for test in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    checked = [[0] * N for _ in range(N)]
    checked[0][0] = 1

    stack = [(0, 0, 0)]

    min_result = float('INF')

    bfs()

    print('#{} {}'.format(test, min_result))
