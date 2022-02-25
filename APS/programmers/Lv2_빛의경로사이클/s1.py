def solution(grid):
    def get_newposition(code, now_dir, row, col):
        if code == 'S':
            dir_lst = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        elif code == 'L':
            dir_lst = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        else:
            dir_lst = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        ni = row + dir_lst[now_dir][0]
        nj = col + dir_lst[now_dir][1]
        return (ni, nj)

    def go(row, col, now_dir):
        nonlocal route_cnt

        if row < 0:
            row += len_row
        elif len_row <= row:
            row -= len_row
        elif col < 0:
            col += len_col
        elif len_col <= col:
            col -= len_col
        
        if check[row][col][now_dir]:
            return

        check[row][col][now_dir] = 1
        route_cnt += 1
        ni, nj = get_newposition(make_matrix[row][col], now_dir, row, col)
        if row > ni:
            new_dir = 0
        elif col > nj:
            new_dir = 1
        elif row < ni:
            new_dir = 2
        else:
            new_dir = 3

        go(ni, nj, new_dir)

    make_matrix = []    # [['S', 'L'], ['L', 'R']]
    check = []          # [[[0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]
    len_row = len(grid)
    for row in grid:
        make_matrix.append(list(row))
        len_col = len(row)
        check.append([[0]*4 for _ in range(len_col)])
     
    answer = []

    for row in range(len_row):      # 모든 경우의 수 탐색! (처음에 (0, 0) 위치에서만 탐색해서 틀림)
        for col in range(len_col):
            for dir_idx in range(4):
                route_cnt = 0
                go(row, col, dir_idx)
                if route_cnt:
                    answer.append(route_cnt)

    answer.sort()
    return answer

k = solution(["R","R"])
print(k)