def solution(m, n, puddles):    
    matrix = [[0] * (m + 1) for _ in range(n + 1)]  # matrix 배열 초기화
    dir = [(0, -1), (-1, 0)]                        # 왼쪽, 위쪽 값

    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if row == 1 and col == 1:       # 집 위치 값 초기화
                matrix[row][col] = 1
                continue
                
            if [col, row] in puddles:       # 침수 된 곳 PASS!
                continue
                
            sum_val = 0     # 왼쪽 + 위쪽 값 변수 초기화
            for k in range(2):
                ni = row + dir[k][0]
                nj = col + dir[k][1]
                if not (0 < ni <= n and 0 < nj <= m):   # 유효성 검사
                    continue
                
                sum_val += matrix[ni][nj]
                    
            matrix[row][col] = sum_val % 1000000007     
            
    return matrix[n][m]