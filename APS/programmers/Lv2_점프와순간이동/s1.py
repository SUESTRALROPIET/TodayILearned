def solution(n):
    ans = 1
    
    while 1 < n:
        if n % 2:
            ans += 1
        n //= 2

    return ans