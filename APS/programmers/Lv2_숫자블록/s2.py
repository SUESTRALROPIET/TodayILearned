def get_num(num):
    if num < 2:
        return 0
    m = int(num ** 0.5)
    for std in range(2, m+1):
        if num % std == 0:
            return num // std
    return 1

def solution(begin, end):
    answer = []
    
    for i in range(begin, end+1):
        answer.append(get_num(i))
    
    return answer