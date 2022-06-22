ans_dict = {}

def solution(n):
    ans = 1
    
    while 1 < n:
        if n in list(ans_dict.keys()):  # 기록
            ans += ans_dict[n]
            break

        if n % 2:
            ans += 1
        n //= 2
    
    ans_dict[n] = ans

    return ans
