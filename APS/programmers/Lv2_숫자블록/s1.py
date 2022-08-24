def get_num(num):
    if num < 2:
        return 0
    for ele in range(2, num):
        if num % ele == 0:
            return num // ele
    return 1

def solution(begin, end):
    answer = []
    
    for k in range(begin, end+1):
        answer.append(get_num(k))

    return answer