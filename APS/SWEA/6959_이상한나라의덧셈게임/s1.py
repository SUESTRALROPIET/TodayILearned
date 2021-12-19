import sys
sys.stdin = open('input.txt')

def next_level(now_str, times):
    global result

    N = len(now_str)

    if N == 1:
        result = times
        return
        
    for start_idx in range(N-1):
        new_num = int(now_str[start_idx]) + int(now_str[start_idx+1])
        new_str = now_str[:start_idx] + str(new_num) + now_str[start_idx+2:]
        
        next_level(new_str, times+1)


T = int(input())
for test in range(1, T+1):
    num_lst = input()

    result = 0

    next_level(num_lst, 1)

    if result % 2:
        winner = 'B'
    else:
        winner = 'A'
    
    print('#{} {}'.format(test, winner))