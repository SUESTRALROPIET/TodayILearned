def solution(a, b, n):
    answer = 0
    
    while n >= a:
        share, remain = divmod(n, a)
        answer += (share * b)
        n = (share * b) + remain

    return answer