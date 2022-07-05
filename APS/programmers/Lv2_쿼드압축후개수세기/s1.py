def solution(arr):
    answer = [0, 0]
    
    N = len(arr)
    is_start = True

    di = [0, 0, 1, 1]
    dj = [0, 1, 0, 1]
    
    while 2 <= N: 
        if is_start:
            matrix = arr
            is_start = False
        
        # 새로운 배열 생성(N//2 길이)
        N //= 2
        new_matrix = [[None] * N for _ in range(N)]
        
        # 전체 배열 탐색하면서 new_matrix에 기록하기
        for row in range(0, N * 2, 2):
            for col in range(0, N * 2, 2):
                cnt = [0, 0]
                for k in range(4):
                    ni = row + di[k]
                    nj = col + dj[k]
                    value = matrix[ni][nj]

                    if value == None:
                        continue

                    cnt[value] += 1
                
                # 새로운 배열에 담거나 answer값 업데이트
                if cnt[0] == 4 or cnt[1] == 4:
                    new_matrix[row//2][col//2] = value
                else:
                    answer[0] += cnt[0]
                    answer[1] += cnt[1]
                    
        matrix = new_matrix
    
    # 마지막 하나 남은 원소 확인하기
    value = matrix[0][0]
    if value != None:
        answer[value] += 1

    return answer