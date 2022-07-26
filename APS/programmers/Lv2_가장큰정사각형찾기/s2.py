def solution(board):
    answer = 0
    
    N = len(board)
    M = len(board[0])
    
    dp = [[0 for _ in range(M)] for _ in range(N)]
    
    for row in range(N):
        for col in range(M):                
            if board[row][col]:
                # if row == 0 or col == 0:      # python에서는 인덱스 번호가 -1이 나와도 분기처리 해줄 필요가 없다.
                #     dp[row][col] = board[row][col]
                # else:
                dp[row][col] = min(dp[row-1][col], dp[row-1][col-1], dp[row][col-1]) + 1
            
            if answer < dp[row][col]:
                answer = dp[row][col]
    return answer ** 2