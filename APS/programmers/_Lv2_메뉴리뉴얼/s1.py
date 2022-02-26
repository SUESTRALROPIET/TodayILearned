def solution(orders, course):
    def dfs(now_status, now_idx, now_len, target_len):
        nonlocal order_lst, len_order_lst, answer
        if now_len == target_len:
            answer[target_len][now_status] = 0

        for new_idx in range(now_idx+1, len_order_lst):
            dfs(now_status+order_lst[new_idx], new_idx, now_len+1, target_len)
            
    answer = [dict() for _ in range(11)]
    
    order_dict = dict()
    for order in orders:
        for order_ele in order:
            if not (order_ele in list(order_dict.keys())):
                order_dict[order_ele] = 1
            else:
                order_dict[order_ele] += 1

    order_lst = []
    for order_key in order_dict:
        if order_dict[order_key] > 1:
            order_lst.append(order_key)
    order_lst.sort()
    len_order_lst = len(order_lst)

    for course_len in course:
        new_lst = ''
        for idx in range(len_order_lst):
            dfs(new_lst+order_lst[idx], idx, 1, course_len)
    
    real_answer = []

    for course_len in course:
        standard_lst = list(answer[course_len].keys())
        for order_ele in orders:
            for standard in standard_lst:
                judge_value = True
                for standard_ele in standard:
                    if not (standard_ele in order_ele):
                        judge_value = False
                    else:
                        continue
                if judge_value:
                    answer[course_len][standard] += 1

        max_value = 0
        if list(answer[course_len].values()):
            if max(list(answer[course_len].values())) > 1:
                max_value = max(list(answer[course_len].values()))
                for answer_ele in answer[course_len]:
                    if answer[course_len][answer_ele] == max_value:
                        real_answer.append(answer_ele)
    real_answer.sort()

    return real_answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))