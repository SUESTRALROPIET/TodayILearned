# 제한시간 초과 => 3개 

import sys
sys.stdin = open('input.txt')

def add_num(start_idx, add_value):          # start_idx가 영향을 주는 idx에 모두 add_value 더하기
    while start_idx < N+1:                              # start_idx: start_idx -> N
        binary_indexed_tree[start_idx] += add_value
        start_idx += (start_idx & -start_idx)           # 마지막 비트가 1인 값 구하기

def cumulativa_sum(idx):                    # 1 ~ idx까지의 누적합 구하기
    cum_sum = 0
    while 0 < idx:
        cum_sum += binary_indexed_tree[idx]
        idx -= (idx & -idx)                             # 마지막 비트가 1인 값 구하기
    return cum_sum

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    input_num = [0] + list(map(int, input().split()))       # 입력받은 숫자들
    binary_indexed_tree = [0] * (N+1)                       # BIT를 적용해서 입력값을 담을 리스트

    result = ''                             # 결과값 저장할 문자열

    for bit_idx in range(1, N+1):               # bit_idx: 1 -> N
        add_num(bit_idx, input_num[bit_idx])
    
    for _ in range(M):
        code, a, b = map(int, input().split())
        if code == 1:
            add_num(a, b)
        else:
            result += ' ' + str(cumulativa_sum(b) - cumulativa_sum(a-1))

    print('#{}{}'.format(test, result))