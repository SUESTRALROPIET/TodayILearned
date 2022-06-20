def solution(number, k):
    N = len(number)
    num_lst = []
    answer = '0'
    
    def comb(start_idx, now_num):
        nonlocal answer
        if len(now_num) == N-k:
            now_num = ''.join(now_num)
            if answer < now_num:
                answer = now_num
            return
        for idx in range(start_idx, N):
            now_num.append(number[idx])
            comb(idx+1, now_num)
            now_num.pop()

    comb(0, num_lst)
    return answer