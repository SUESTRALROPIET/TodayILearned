MAX_N = 20
fac_lst = [0 for _ in range(MAX_N)]
fac_lst[1] = 1
for i in range(2, MAX_N):
    fac_lst[i] = fac_lst[i-1] * i
    
def solution(n, k):
    num_lst = [i for i in range(1, n+1)]
    answer = []
    
    step = n - 1
    
    while step:
        idx = (k - 1) // fac_lst[step]
        answer.append(num_lst[idx])
        k -= (idx * fac_lst[step])
        del(num_lst[idx])
    
        step -= 1
        
    return answer + num_lst