# 2진수 변환시 '1' 개수 반환
def get_one(n):
    cnt = 0
    while n:
        cnt += n % 2
        n //= 2
    return cnt

def solution(n):    
    n_cnt = get_one(n)
    K = n+1
    
    while True:
        k_cnt = get_one(K)
        if k_cnt == n_cnt:
            return K
        K += 1