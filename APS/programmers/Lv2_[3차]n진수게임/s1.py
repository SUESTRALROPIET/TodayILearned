def get_transition(num, n):     # num을 n진수로 변환 후, string으로 반환
    return_str = ''
    while num:
        remain = num % n
        if remain > 9:
            remain += 55
            remain = chr(remain)
            
        return_str = str(remain) + return_str
        num //= n
    
    return return_str

def solution(n, t, m, p):
    # m명이 t번 반복
    total_transition = '0'
    num = 1
    while len(total_transition) < t * m:
        total_transition += get_transition(num, n)
        num += 1
    
    # p번째 사람이 말해야할 값 t
    answer = ''
    N = len(total_transition)
    for idx in range(p-1, N, m):
        answer += (total_transition[idx])
        if len(answer) == t:
            return answer