import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N, S = input().split()
    N = int(N)
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = [[0] * N for _ in range(N)]
    
    if S == 'up':
        for col_idx in range(N):        # col_idx: 0 > N-1
            result_idx = 0                  # 결과값 idx
            now_status = 0                  # 현재 matrix 숫자
            for row_idx in range(N):            # row_idx: 0 > N-1
                if not now_status:
                    now_status = matrix[row_idx][col_idx]
                    continue

                if matrix[row_idx][col_idx] == 0:
                    continue

                if matrix[row_idx][col_idx] == now_status:
                    result[result_idx][col_idx] = now_status * 2
                    result_idx += 1
                    now_status = 0
                else:
                    result[result_idx][col_idx] = now_status
                    now_status = matrix[row_idx][col_idx]
                    result_idx += 1

            if now_status:
                result[result_idx][col_idx] = now_status
     
    elif S == 'down':
        for col_idx in range(N):        
            result_idx = N-1                  
            now_status = 0                  
            for row_idx in range(N-1, -1, -1):            
                if not now_status:
                    now_status = matrix[row_idx][col_idx]
                    continue

                if matrix[row_idx][col_idx] == 0:
                    continue

                if matrix[row_idx][col_idx] == now_status:
                    result[result_idx][col_idx] = now_status * 2
                    result_idx -= 1
                    now_status = 0
                else:
                    result[result_idx][col_idx] = now_status
                    now_status = matrix[row_idx][col_idx]
                    result_idx += 1

            if now_status:
                result[result_idx][col_idx] = now_status

    elif S == 'left':
        for row_idx in range(N):        
            result_idx = 0                
            now_status = 0                 
            for col_idx in range(N):           
                if not now_status:
                    now_status = matrix[row_idx][col_idx]
                    continue

                if matrix[row_idx][col_idx] == 0:
                    continue

                if matrix[row_idx][col_idx] == now_status:
                    result[row_idx][result_idx] = now_status * 2
                    result_idx += 1
                    now_status = 0
                else:
                    result[row_idx][result_idx] = now_status
                    now_status = matrix[row_idx][col_idx]
                    result_idx += 1

            if now_status:
                result[row_idx][result_idx] = now_status

    elif S == 'right':
        for row_idx in range(N):        
            result_idx = N-1                 
            now_status = 0                 
            for col_idx in range(N-1, -1, -1):           
                if not now_status:
                    now_status = matrix[row_idx][col_idx]
                    continue

                if matrix[row_idx][col_idx] == 0:
                    continue

                if matrix[row_idx][col_idx] == now_status:
                    result[row_idx][result_idx] = now_status * 2
                    result_idx -= 1
                    now_status = 0
                else:
                    result[row_idx][result_idx] = now_status
                    now_status = matrix[row_idx][col_idx]
                    result_idx += 1

            if now_status:
                result[row_idx][result_idx] = now_status
                
    print('#{}'.format(test))
    for row_lst in result:
        print(*row_lst)