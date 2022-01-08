# 제한시간 초과 => 3개 

import sys
sys.stdin = open('input.txt')

def add_num(start_idx, add_value):
    while start_idx < N+1:
        binary_indexed_tree[start_idx] += add_value
        start_idx += start_idx & -start_idx

def cumulativa_sum(idx):
    cum_sum = 0
    while 0 < idx:
        cum_sum += binary_indexed_tree[idx]
        idx -= idx & -idx
    return cum_sum

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    input_num = [0] + list(map(int, input().split()))
    binary_indexed_tree = [0] * (N+1)

    result = ''

    for bit_idx in range(1, N+1):
        add_num(bit_idx, input_num[bit_idx])
        # print(binary_indexed_tree)
    
    # print(binary_indexed_tree)
    
    for _ in range(M):
        code, a, b = map(int, input().split())
        if code == 1:
            add_num(a, b)
            # print(binary_indexed_tree)
        else:
            result += ' ' + str(cumulativa_sum(b) - cumulativa_sum(a-1))

    print('#{}{}'.format(test, result))