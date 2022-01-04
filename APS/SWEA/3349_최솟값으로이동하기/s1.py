import sys
sys.stdin = open('input.txt')

def get_distance(now_x, now_y, target_x, target_y, cnt):
    global part_result

    if part_result <= cnt:
        return

    if now_x == target_x and now_y == target_y:
        if cnt < part_result:
            part_result = cnt
        return
    
    di = [-1, 1, 0, 1, 0, -1]
    dj = [-1, 1, 1, 0, -1, 0]

    for k in range(6):
        ni = now_x + di[k]
        nj = now_y + dj[k]
        
        if not (0 < ni <= W and 0 < nj <= H):
            continue

        if visited[ni][nj]:
            continue
        
        visited[ni][nj] = 1
        get_distance(ni, nj, target_x, target_y, cnt+1)
        visited[ni][nj] = 0


T = int(input())
for test in range(1, T+1):
    W, H, N = map(int, input().split())

    result = 0

    start_x, start_y = map(int, input().split())

    for _ in range(N-1):
        new_x, new_y = map(int, input().split())
        part_result = W * H

        visited = [[0] * (H+1) for _ in range(W+1)]
        
        visited[start_x][start_y] = 1
        get_distance(start_x, start_y, new_x, new_y, 0)

        start_x, start_y = new_x, new_y
        result += part_result

    print('#{} {}'.format(test, result))
