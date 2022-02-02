def solution(s):
    answer = -1
    s = list(s)
    s_len = len(s)
    new_len = 0
    
    while s_len != new_len:
        s_len = len(s)
        for i in range(s_len-1):
            if s[i] == s[i+1]:
                s.pop(i)
                s.pop(i)
                new_len = len(s)
                break
            else:
                new_len = len(s)
                continue
    if s_len:
        answer = 0
    else:
        answer = 1
        
    return answer