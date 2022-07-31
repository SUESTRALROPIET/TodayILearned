def solution(arr):
    min_val = 0
    max_val = 0
    
    N = len(arr)
    now_sum = 0
    
    for idx in range(N-1, -1, -1):
        if arr[idx] == '+':
            continue

        elif arr[idx] == '-':
            nxt_ele = int(arr[idx+1])
            
            a = -now_sum + min_val      # 최솟값 경우 1
            b = -(now_sum + max_val)    # 최솟값 경우 2
            c = -(now_sum + min_val)                # 최댓값 경우 1
            d = now_sum - (2 * nxt_ele) + max_val   # 최댓값 경우 2

            min_val = min(a, b)
            max_val = max(c, d)
            
            now_sum = 0     # 누적값 초기화

        else:
            now_sum += int(arr[idx])
    
    return max_val + now_sum