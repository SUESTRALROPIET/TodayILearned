def solution(expression):
    def cal(fst, op, scd):
        if op == '*':
            return fst * scd
        elif op == '+':
            return fst + scd
        else:
            return fst - scd

    def get_cal(ordered_op_lst):
        nonlocal max_value
        wait_stack = []
        remain_stack = []
        remain_stack += input_stack

        for op in ordered_op_lst:
            while remain_stack:
                now_ele = remain_stack.pop(0)
                if type(now_ele) == int and 0 <= now_ele <= 999:
                    wait_stack.append(now_ele)
                elif now_ele == op:
                    cal_value = cal(wait_stack.pop(), now_ele, remain_stack.pop(0))
                    wait_stack.append(cal_value)
                else:
                    wait_stack.append(now_ele)

            remain_stack = wait_stack
            wait_stack = []

        if max_value < abs(remain_stack[0]):
            max_value = abs(remain_stack[0])

    def order_op(n):
        if n == 3:
            return get_cal(ordered_op)
        for i in range(3):
            if op_checked[i]:
                continue
            else:
                op_checked[i] = 1
                ordered_op[n] = op_lst[i]
                order_op(n+1)
                op_checked[i] = 0

    def make_stack(input_str):
        now_num = ''
        input_stack = []
        input_lst = list(input_str)

        for ele in input_lst:
            if '0' <= ele <= '9':
                now_num += ele
            else:
                input_stack.append(int(now_num))
                input_stack.append(ele)
                now_num = ''
        input_stack.append(int(now_num))
        return input_stack

    op_lst = ['*', '+', '-']
    ordered_op = [''] * 3
    op_checked = [0] * 3
    max_value = 0
    input_stack = make_stack(expression)
    order_op(0)
    
    return max_value
