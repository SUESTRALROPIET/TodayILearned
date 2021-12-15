import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, 2):
    p, q = map(int, input().split())

    brackets_dict = {
        'r_cnt': 0,
        'c_cnt': 0,
        's_cnt': 0,
    }

    R = C = S = 0
    dot_cnt = 0

    for idx in range(p):
        print(brackets_dict, dot_cnt)

        dot_start = True
        dot_cnt = 0
        text_list = list(input())
        for ele in text_list:
            if ele == '.' and dot_start:
                dot_cnt += 1
                continue
            elif ele == '(':
                brackets_dict['r_cnt'] += 1
            elif ele == ')':
                brackets_dict['r_cnt'] -= 1
            elif ele == '{':
                brackets_dict['c_cnt'] += 1
            elif ele == '}':
                brackets_dict['c_cnt'] -= 1
            elif ele == '[':
                brackets_dict['s_cnt'] += 1
            elif ele == ']':
                brackets_dict['s_cnt'] -= 1

            dot_start = False

    for idx in range(q):
        a = input()

            



