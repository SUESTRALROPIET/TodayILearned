import sys
sys.stdin = open('input.txt')

import math

def get_part_sum(idx):
    k = max_idx -1 
    part_sum = 0
    
    while 1 < k:
        part_sum += data[idx - k]
        k //= 2
    return part_sum

def add_num(idx, num):
    data[data_N] += num
    now_idx = data_N

    k = max_idx
    while 0 <= k:
        if idx < now_idx - (2**k) and now_idx - (2**k) <= N:
            data[now_idx - (2**k)] += num 
            now_idx -= (2**k)
        k -= 1

    data[idx] += num

def get_sum(idx):
    new_sum = 0
    k = max_idx
    while 0 < k:
        if data_N - (2**k) < idx:
            new_sum += data[data_N - 2**k]
        k -= 1
    new_sum += data[idx]
    return new_sum

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    input_lst = [0] + list(map(int, input().split()))

    max_idx = math.ceil(N ** 0.5)
    data_N = 2 ** max_idx
    data = [0] * (data_N + 1)

    for idx in range(1, N+1):
        if idx % 2:
            data[idx] = input_lst[idx]
        elif idx % 4:
            data[idx] = input_lst[idx-1] + input_lst[idx]
        else:
            print(idx, get_part_sum(idx),input_lst[idx-1] , input_lst[idx])
            data[idx] = get_part_sum(idx) + input_lst[idx-1] + input_lst[idx]
    print(data)
    result = ''
    for _ in range(M):
        code, a, b = map(int, input().split())

        if code == 1:
            add_num(a, b)
            print(data)

        else:
            result += ' ' + str(get_sum(b) - get_sum(a-1))
    

    print('#{}{}'.format(test, result))

