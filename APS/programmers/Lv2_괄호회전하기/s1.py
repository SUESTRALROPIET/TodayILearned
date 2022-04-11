def solution(s):
    def check(stack):
        open_ele = ['(', '[', '{']  # 열린 괄호

        std_dict = dict()       # 짝맞추어 닫힌 괄호 dict에 담기
        std_dict['('] = ')'
        std_dict['['] = ']'
        std_dict['{'] = '}'

        remain_stack = []

        for ele in stack:   # 하나씩 탐색
            if ele in open_ele:     # 열린 괄호면, remain_stack에 담기
                remain_stack.append(ele)
                continue
            if remain_stack:        # 닫힌 괄호이고, remain_stack이 있으면
                now_ele = remain_stack.pop()    # remain_stack에서 꺼내서
                if ele != std_dict[now_ele]:    # dict값과 다르면 False => 짝 아님
                    return False
            else:                   # 닫힌 괄호이고, remain_stack이 없으면 => 짝 없음
                return False
                
        if remain_stack:    # 열린괄호가 아직 remain_stack에 남아있으면 => 짝 없음
            return False
        return True
            
    answer = 0
    
    N = len(s)
    for start_idx in range(N):
        stack = s[start_idx:] + s[:start_idx]
        if check(stack):
            answer += 1
    return answer
