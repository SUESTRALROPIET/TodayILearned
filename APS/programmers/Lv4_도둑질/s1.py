def solution(money):    
    N = len(money)
    fst = [0] + money[:-1]
    scd = [0] + money[1:]
    
    for idx in range(2, N):      
        fst[idx] = max(fst[idx]+fst[idx-2], fst[idx-1])
        scd[idx] = max(scd[idx]+scd[idx-2], scd[idx-1])
        
    return max(fst[-1], scd[-1])