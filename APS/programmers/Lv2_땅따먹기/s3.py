# def solution(land):
#     N = len(land)

#     for row in range(N-1, 0, -1):
#         answer = land[row-1]
        
#         answer[0] += max(land[row][1], land[row][2], land[row][3])
#         answer[1] += max(land[row][0], land[row][2], land[row][3])
#         answer[2] += max(land[row][0], land[row][1], land[row][3])
#         answer[3] += max(land[row][0], land[row][1], land[row][2])
        

#     return max(answer)


def solution(land):
    N = len(land)

    for row in range(N-1, 0, -1):
        answer = land[row-1]        # 아래 최대값 구하는 행의 앞 행
        
        for col in range(4):
            answer[col] += max(land[row][:col] + land[row][col+1:])     
    return max(answer)