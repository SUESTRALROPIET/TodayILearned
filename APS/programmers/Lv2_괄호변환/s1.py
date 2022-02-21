def solution(p):
    answer = ''
    value_dict = {'(': 1, ')': -1}

    def is_correct(input_str):
        now_value = 0
        for ele in input_str:
            now_value += value_dict[ele]
            if now_value < 0:
                return False
        else:
            return True

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
    
    answer_len = len(answer_lst)
    for answer_idx in range(answer_len-1, -1, -1):
        if is_correct(answer_lst[answer_idx]):
            answer = answer_lst[answer_idx] + answer
        else:
            answer = '(' + answer + ')'
            for answer_ele in answer_lst[answer_idx][1:-1]:
                value_dict_keys=list(value_dict.keys())
                if answer_ele == value_dict_keys[0]:
                    answer += value_dict_keys[1]
                else:
                    answer += value_dict_keys[0]

    return answer

