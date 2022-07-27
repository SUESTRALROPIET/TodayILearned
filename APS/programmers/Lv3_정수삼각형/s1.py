def solution(triangle):    
    N = len(triangle)

    dp = []
    for k in range(1, N+1):     # dp 테이블 초기화
        dp.append([0] * k)
    
    dp[0][0] = triangle[0][0]   # 첫 행값 초기화
    
    for row in range(1, N):
        for col in range(row+1):
            now_num = triangle[row][col]
            if col == 0:
                now_num += dp[row-1][0]
            elif col == row:
                now_num += dp[row-1][row-1]
            else:
                now_num += max(dp[row-1][col-1], dp[row-1][col])         
                       
            dp[row][col] = now_num
            
    return max(dp[N-1])