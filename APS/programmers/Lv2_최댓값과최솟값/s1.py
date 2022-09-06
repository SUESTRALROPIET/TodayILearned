def solution(s):    
    max_num = float('-inf')
    min_num = float('inf')
    
    s = s.split(" ")

    for num in s:
        num = int(num)
        if max_num < num:
            max_num = num
        if num < min_num:
            min_num = num
            
    answer = [min_num, max_num]
    answer = ' '.join(map(str, answer))
        
    return answer