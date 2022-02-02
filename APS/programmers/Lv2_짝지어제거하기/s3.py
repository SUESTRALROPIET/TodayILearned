from copy import deepcopy

def solution(s):
    stack = list(s)
    stack_lst = []

    while 1 < len(stack):
        if stack in stack_lst:
            break
        else:
            stack_lst.append(deepcopy(stack))

        fst = stack.pop(0)
        scd = stack[0]
        if fst == scd:
            stack.pop(0)
            continue
        else:
            stack.append(fst)

    if stack:
        return 0
    else:
        return 1
