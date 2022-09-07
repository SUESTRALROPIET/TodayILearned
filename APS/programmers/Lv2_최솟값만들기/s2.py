def solution(A,B):
    answer = 0
    
    N = len(A)

    A.sort()
    B.sort(reverse=True)
    
    for a, b in zip(A, B):
        answer += (a * b)
    
    return answer