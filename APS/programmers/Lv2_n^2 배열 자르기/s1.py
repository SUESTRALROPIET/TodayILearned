def solution(n, left, right):
    
    def return_num(num):    # idx에 해당하는 수 반환하기
        share, remain = divmod(num, n)
        if remain <= share:
            return share + 1
        else:
            return remain + 1
    
    answer = []
    
    for idx in range(left, right+1):
        answer.append(return_num(idx))
    
    return answer