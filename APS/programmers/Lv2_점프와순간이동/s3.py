def solution(n):
    ans = 1
    
    while 1 < n:
        ans += n % 2
        n //= 2

    return ans