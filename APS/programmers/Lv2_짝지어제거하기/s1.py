def solution(s):
    answer = -1
    s = list(s)
    input_len = len(s)
    new_len = 0
    
    while True:
        if new_len == input_len:
            break
        input_len = len(s)
        for i in range(input_len-1):
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                new_len = len(s)
                break
            new_len = len(s)
                
    if new_len == 0:
        answer = 1
    else:
        answer = 0
        
    return answer