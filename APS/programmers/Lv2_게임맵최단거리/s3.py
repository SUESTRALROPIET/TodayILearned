def solution(maps):
    row_len = len(maps)     # 행 길이
    col_len = len(maps[0])  # 열 길이
    # visited = [[0] * col_len for _ in range(row_len)]  ### visited => 시간초과 1

    stack = [(0, 0, 1)]     # 시작지점
    maps[0][0] = 0          # 탐색 완료 표시: 벽(0)으로 값 변경
    answer = row_len * col_len * 2  # 최대값

    while stack:
        row, col, cnt = stack.pop(0)
        # visited[row][col] = 1
        # maps[row][col] = 0                             ### 꺼낼때마다 0으로 값 변경 => 시간초과 2

        if answer <= cnt:   # cnt가 answer 보다 크면 더 이상 탐색 X
            continue 

        if row == row_len-1 and col == col_len-1:   # 목적지에 도달하면,
            if cnt < answer:                            # cnt & answer 값 비교 후, answer 값 갱신                    
                answer = cnt    
            continue

        di = [0, 1, 0, -1]  # 우 / 하 / 좌 / 상
        dj = [1, 0, -1, 0]
        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if not (0 <= ni < row_len and 0 <= nj < col_len):   # 유효성 검사
                continue
            if maps[ni][nj] == 0:                               # 벽(0)인지 검사
                continue
            
            maps[ni][nj] = 0                        ### 탐색할 곳 list에 담으면서 모두 벽(0)으로 값 변경: 다른 방향에서 탐색/append 못 하도록 하기
            stack.append((ni, nj, cnt+1))

    # 초기값이면 -> 목적지 도달 X
    if answer == row_len * col_len * 2:     ### 처음에 row_len*col_len 만 해줘서 n 또는 m이 1일때 벽이 없는 map에서 틀림
        answer = -1

    return answer

