def cal(a, b, c):
    a = int(a)
    c = int(c)
    if b == '+':
        return a + c
    else:
        return a - c

def solution(arr):
    def get_cal(lst): 
        nonlocal answer          

        N = len(lst)
        
        if N == 3:
            result = cal(*lst)
            if answer < result:
                answer = result
            return
        
        for idx in range(0, N-2, 2):
            perm_result = cal(*lst[idx : idx+3])
            get_cal(lst[:idx] + [perm_result] + lst[idx+3:])
    
    answer = float('-INF')
    
    get_cal(arr)
    
    return answer


arr = ["1", "-", "3", "+", "5", "-", "8"]
print(solution(arr))