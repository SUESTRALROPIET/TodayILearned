def solution(s):
    answer = True
    cnt_dic = {'(': 0, ')': 0}
    
    for ele in s:
        cnt_dic[ele] += 1
        
        if cnt_dic['('] < cnt_dic[')']:     # 오른쪽 괄호가 넘치면 => False
            return False  

    if cnt_dic['('] > cnt_dic[')']:    # 왼쪽 괄호가 넘치면 => False
        return False
    
    return True