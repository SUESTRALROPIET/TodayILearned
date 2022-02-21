def solution(expression):
    def cal(fst, op, scd):  # 연산자로 계산한 값을 반환하기
        if op == '*':
            return fst * scd
        elif op == '+':
            return fst + scd
        else:
            return fst - scd

    def get_cal(ordered_op_lst):
        nonlocal max_value
        wait_stack = []     # 아직 계산될 차례가 되지 않은 피연산자/연산자들 stack
        remain_stack = []   # 남은 연산자/피연산자
        remain_stack += input_stack     #  remain_stack 초기화

        for op in ordered_op_lst:   #  연산자 순서대로 반복하면서 (예)['*', '+', '-']
            while remain_stack:         # reamain_stack을 모두 다 소진할 때까지 반복
                now_ele = remain_stack.pop(0)       # now_ele => 현재 값
                if type(now_ele) == int and 0 <= now_ele <= 999:    # 현재값이 숫자이면 => wait_stack에 추가
                    wait_stack.append(now_ele)
                elif now_ele == op:                                 # 현재값이 지금 연산자(op)이면
                    cal_value = cal(wait_stack.pop(), now_ele, remain_stack.pop(0))     # 계산해서
                    wait_stack.append(cal_value)                                        # wait_stack에 추가하기
                else:                                               # 현재값이 지금 연산자가 아니면
                    wait_stack.append(now_ele)                          # wait_stack에 추가

            remain_stack = wait_stack   # wait_stack에 있는 값 remain_stack에 옮겨서 다음 연산자로 재탐색
            wait_stack = []             # wait_stack 초기화

        if max_value < abs(remain_stack[0]):    # 모든 계산이 끝났을 때 max_value와 비교해서
            max_value = abs(remain_stack[0])        # max_value에 큰값 반환

    def order_op(n):    # 연산자 정렬하기
        if n == 3:          # 모든 연산자를 정렬했다면
            return get_cal(ordered_op)  # 계산하러 가기!
        for i in range(3):
            if op_checked[i]:
                continue
            else:
                op_checked[i] = 1
                ordered_op[n] = op_lst[i]
                order_op(n+1)
                op_checked[i] = 0

    def make_stack(input_str):
        now_num = ''                # 현재 값
        input_stack = []            # input_stack 초기화
        input_lst = list(input_str) # input 문자열값 list로 변환

        for ele in input_lst:       # input_lst 반복하면서
            if '0' <= ele <= '9':       # 숫자면 now_num에 추가
                now_num += ele
            else:                       # 문자열(연산자)이면
                input_stack.append(int(now_num))    # now_num 숫자로 변환하여 stack에 추가
                input_stack.append(ele)             # 연산자 stack에 추가
                now_num = ''                        # now_num  초기화
        input_stack.append(int(now_num))    # 남은 마지막 피연산자 숫자로 변환하여 stack에 추가
        return input_stack  # 숫자/연산자로 분리시킨 input_stack 반환

    op_lst = ['*', '+', '-']        # 전체 연산자 리스트
    ordered_op = [''] * 3           # 연산자를 정렬할 빈 리스트
    op_checked = [0] * 3            # 연산자 정렬 여부 체크

    max_value = 0                   # 최대값 초기화
    input_stack = make_stack(expression)    # input값 숫자 / 부호로 나누어 input_stack에 담기
    order_op(0)                     # 연산자 정렬시키면서 계산하기
    
    return max_value
