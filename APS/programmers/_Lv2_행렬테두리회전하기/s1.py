import copy

def solution(rows, columns, queries):    
    def change(now_i, now_j, query, k):
        nonlocal min_result

        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        start_x,start_y, end_x, end_y = query

        ni = now_i + di[k%4]
        nj = now_j + dj[k%4]

        if 3 < k:
            return

        if start_x <= ni <= end_x and start_y <= nj <= end_y:   # 정해진 구간 안에서 시계방향으로 이동
            matrix_value = matrix[now_i][now_j]
            new_matrix[ni][nj] = matrix_value
            if matrix_value < min_result:
                min_result = matrix_value
            return change(ni, nj, query, k)

        else:                                                   # 구간이 벗어나면 k를 증가시켜 방향 전환
            return change(now_i, now_j, query, k+1)
        
    matrix = [[0] + [0] * columns for _ in range(rows+1)]
    
    for col in range(1, rows+1):
        for row in range(1, columns+1):
            matrix[col][row] = columns * (col-1) + row

    answer = []
    new_matrix = copy.deepcopy(matrix)
    for query in queries:
        min_result = float('INF')
        change(query[0], query[1], query, 0)
        matrix = copy.deepcopy(new_matrix)
        answer.append(min_result)

    return answer