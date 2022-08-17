def solution(topping):
    N = len(topping)
    left = [0 for _ in range(N+1)]
    right = [0 for _ in range(N+1)]

    cnt = 0
    left_lst = []
    for idx in range(N):
        ele = topping[idx]
        if ele not in left_lst:
            left_lst.append(ele)
            cnt += 1
        left[idx] = cnt
    cnt = 0
    right_lst = []
    for idx in range(N-1, -1, -1):
        ele = topping[idx]
        if ele not in right_lst:
            right_lst.append(ele)
            cnt += 1
        right[idx] = cnt
    
    answer = 0
    for idx in range(N):
        if left[idx] == right[idx+1]:
            answer += 1
    return answer