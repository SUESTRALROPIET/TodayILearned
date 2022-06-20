import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(target, record_table):
    row, col = target
    record_table[row][col] = 0

    q = [(0, row, col)]

    while q:
        cnt, now_row, now_col = heapq.heappop(q)

        # 탐색한 곳이면 pass
        if record_table[now_row][now_col] < cnt:
            continue
        
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        for k in range(4):
            ni = now_row + di[k]
            nj = now_col + dj[k]

            if not (0 <= ni < h+2 and 0 <= nj < w+2):
                continue
            if matrix[ni][nj] == '*':
                continue
            if matrix[ni][nj] == '#':
                new_cnt = cnt + 1
            else:
                new_cnt = cnt

            ### 비교 후 더 작은 값 기록 + heappush로 추가
            if new_cnt < record_table[ni][nj]:
                record_table[ni][nj] = new_cnt
                heapq.heappush(q, (new_cnt, ni, nj))

T = int(input())

for _ in range(T):
    h, w = map(int, input().split())
    matrix = [['.'] * (w+2)] + [['.'] + list(input()) + ['.'] * (w+2) + ['.'] for _ in range(h)] + [['.'] * (w+2)]

    record = [[[float('INF')] * (w + 2) for _ in range(h + 2)] for _ in range(3)]
    targets = [(0, 0)]
    for i in range(h+2):
        for j in range(w+2):
            if matrix[i][j] == '$':
                targets.append((i, j))

    for idx in range(3):
        dijkstra(targets[idx], record[idx])

    for col_idx in range(h+2):
        record[0][col_idx] = [x + y + z for x, y, z in zip(record[0][col_idx], record[1][col_idx], record[2][col_idx])]

    # 최소값 구하기
    answer = float('INF')
    for i in range(h+2):
        for j in range(w+2):
            cnt = record[0][i][j]
            if matrix[i][j] == '#':
                cnt -= 2
            if cnt < answer:
                answer = cnt

    print(answer)