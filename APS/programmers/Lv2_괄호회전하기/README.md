## Lv.2 괄호 회전하기

https://programmers.co.kr/learn/courses/30/lessons/76502

#### 1. index 슬라이싱해서 짝맞는지 검사하기
```python
def solution(s):
    def check(stack):
        open_ele = ['(', '[', '{']

        std_dict = dict()
        std_dict['('] = ')'
        std_dict['['] = ']'
        std_dict['{'] = '}'

        remain_stack = []

        for ele in stack:
            if ele in open_ele:
                remain_stack.append(ele)
                continue
            if remain_stack:
                now_ele = remain_stack.pop()
                if ele != std_dict[now_ele]:
                    return False
            else:
                return False
                
        if remain_stack:
            return False
        return True
            
    answer = 0
    
    N = len(s)
    for start_idx in range(N):
        stack = s[start_idx:] + s[:start_idx]
        if check(stack):
            answer += 1
    return answer
```
