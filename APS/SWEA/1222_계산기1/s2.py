import sys
sys.stdin = open('input.txt')

for test in range(1, 11):
    N = int(input())
    input_list = list(input())

    # 후위 표기식으로 변환하기
    op_stack = []
    postfix = ''

    while 0 < len(input_list):
        ele = input_list.pop(0)
        if ele.isdigit():
            postfix += ele
        elif op_stack:
            postfix += op_stack.pop()
            op_stack.append(ele)
        else:
            op_stack.append(ele)
    postfix += op_stack.pop()

    num_stack = []
    for ele in postfix:
        if ele.isdigit():
            num_stack.append(ele)
        else:
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(int(a)+int(b))

    print('#{}'.format(test), *num_stack)
