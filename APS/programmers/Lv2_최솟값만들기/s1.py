def solution(A,B):
    answer = 0
    
    N = len(A)

    A.sort()
    B.sort()
    
    for idx in range(N):
        answer += (A[idx] * B[N-1-idx])
    
    return answer