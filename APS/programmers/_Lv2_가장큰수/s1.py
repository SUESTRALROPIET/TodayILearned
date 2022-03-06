def solution(numbers):
    answer = '0'
    
    def get_num(now_lst, level):
        nonlocal answer
        if level == N:
            new_num = ''.join(now_lst)
            if answer < new_num:
                answer = new_num
            return
        for idx in range(N):
            if check[idx]:
                continue
            else:
                check[idx] = 1
                get_num(now_lst+[numbers[idx]], level+1)
                check[idx] = 0

    N = len(numbers)
    for idx in range(N):
        numbers[idx] = str(numbers[idx])
    
    check = [0] * N
    get_num([], 0)  
    
    return answer