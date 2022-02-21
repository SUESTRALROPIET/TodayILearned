## Lv.2 괄호변환

https://programmers.co.kr/learn/courses/30/lessons/60058

#### 1. 순차적으로 풀기

> 1. 균형잡힌 괄호 문자열 기준으로 입력값 분해
> 2. 올바른 괄호 문자열인지 탐색
> 3. 올바른 괄호 문자열이 아닌 경우 문제에 적힌 과정을 참고하여 수정 후 반환

```python
def solution(p):
    answer = ''
    value_dict = {'(': 1, ')': -1}      # 괄호에 값 지정하기

    # 올바른 괄호 문자열이면 True 반환 / 아니면 False 반환
    def is_correct(input_str):
        now_value = 0
        for ele in input_str:
            now_value += value_dict[ele]
            if now_value < 0:
                return False
        else:
            return True

    # 주어진 값 균형잡힌 괄호 문자열로 나누기
    def divide_uv(input_str):
        input_str_len = len(input_str)
        u = ''
        v = ''
        now_value = 0
        for input_idx in range(input_str_len):
            now_value += value_dict[input_str[input_idx]]
            u += input_str[input_idx]
            if now_value == 0:
                v = input_str[input_idx+1:]
                return (u, v)

    answer_lst = []
    while True:
        now_u, now_v = divide_uv(p)
        p = now_v
        answer_lst.append(now_u)
        if now_v == '':
            break

    # 주어진 값 균형잡힌 괄호 문자열로 나누기
    answer_len = len(answer_lst)
    for answer_idx in range(answer_len-1, -1, -1):  # 균형잡힌 괄호 문자열 리스트 뒤에서부터 탐색하기
        if is_correct(answer_lst[answer_idx]):      # 올바른 괄호 문자열이면 answer에 그대로 붙이기
            answer = answer_lst[answer_idx] + answer
        else:                                       # 올바른 괄호 문자열이 아니면 (문제에 적힌 과정 참고)
            answer = '(' + answer + ')'                 # 현재 answer에 양쪽에 괄호 붙이고
            for answer_ele in answer_lst[answer_idx][1:-1]: # 양끝 제외하고 남은 문자열 '(' -> ')' / ')' -> '(' 로 붙이기
                value_dict_keys = list(value_dict.keys())
                if answer_ele == value_dict_keys[0]:
                    answer += value_dict_keys[1]
                else:
                    answer += value_dict_keys[0]

    return answer
```



