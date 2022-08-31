def solution(n, k):
    def get_comb(depth, arr):
        nonlocal idx, answer
        
        if depth == n+1:
            idx += 1
            if idx == k:
                answer = arr
            return
        
        for num in range(n):
            if checked[num]: continue

            checked[num] = True
            get_comb(depth+1, arr + [num_lst[num]])
            checked[num] = False
        
    answer = []
    idx = 0
    num_lst = [i for i in range(1, n+1)]
    checked = [False for _ in range(n)]
    
    get_comb(1, [])
    
    return answer
