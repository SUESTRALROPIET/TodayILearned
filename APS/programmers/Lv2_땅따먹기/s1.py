def solution(land):
    def dfs(row_idx, col_idx, total):
        nonlocal answer
        
        if row_idx == N:
            if answer < total:
                answer = total
            return
            
        for idx in range(4):
            if idx == col_idx:
                continue
            
            dfs(row_idx + 1, idx, total+land[row_idx][idx])
        
    answer = 0
    N = len(land)
    dfs(0, -1, 0)
    
    return answer