def solution(maps):
    row_len = len(maps)
    col_len = len(maps[0])
    visited = [[0] * col_len for _ in range(row_len)]
    visited[0][0] = 1

    def dfs(row, col, cnt):
        nonlocal answer

        if answer <= cnt:
            return 
        if row == row_len-1 and col == col_len-1:
            if cnt < answer:
                answer = cnt
            return

        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if not (0 <= ni < row_len and 0 <= nj < col_len):
                continue
            if maps[ni][nj]==0 or visited[ni][nj]:
                continue
            visited[ni][nj] = 1
            dfs(ni, nj, cnt+1)
            visited[ni][nj] = 0
        return

    answer = row_len * col_len * 2
    
    dfs(0, 0, 1)

    if answer == row_len * col_len * 2: # 처음에 row_len*col_len 만 해줘서 n 또는 m이 1일때 벽이 없는 map에서 틀림
        answer = -1

    return answer

print(solution([[1, 1, 1]]))