def solution(board):
    def find_square(row, col, cnt):
        nonlocal answer
        
        nj = col + 1
        if j <= nj < C and board[row][nj] == 1:
            find_square(row, nj, cnt+1)
        
        square = cnt ** 2
        
        if answer >= square:
            return
        
        if row + cnt > R or j + cnt > C:
            return
        
        for k in range(cnt):
            # for l in range(cnt):
                # if board[row+k][j+l] == 0:
                #     return
            if 0 in board[row+k][j:j+cnt]:
                return
        
        answer = square
        return

    answer = 0
    
    R = len(board)
    C = len(board[0])
    for i in range(R):
        for j in range(C):
            if board[i][j] == 1:
                find_square(i, j, 1)
    
    return answer