def solution(m, n, board):
    answer = 0
    
    checked = [[0] * n for _ in range(m)]
    total_check_lst = []

    def check_board(m, n, board):
        nonlocal total_check_lst
        for row in range(m-1):
            for col in range(n-1):
                if checked[row][col] == 'x':
                    continue
                center = board[row][col]
                # 아래
                bottom_row = row + 1
                while bottom_row < m - 1 and checked[bottom_row][col] == 'x':
                    bottom_row += 1
                if m <= bottom_row or board[bottom_row][col] != center:
                    continue
                right_row = bottom_row
                while 0 < right_row and checked[right_row][col + 1] == 'x':
                    right_row -= 1
                if right_row < 0 or board[right_row][col + 1] != center:
                    continue
                right_row -= 1
                while 0 < right_row and checked[right_row][col + 1] == 'x':
                    right_row -= 1
                if right_row < 0 or board[right_row][col + 1] != center:
                    continue
                total_check_lst += [(row, col), (bottom_row, col), (bottom_row, col+1), (right_row, col+1)]
        # print(total_check_lst)
        if total_check_lst:
            for check in total_check_lst:
                checked[check[0]][check[1]] = 'x'
            total_check_lst = []
            check_board(m, n, board)
        else:
            return
    
    check_board(m, n, board)

    for row in range(m):
        answer += checked[row].count('x')
    return answer
