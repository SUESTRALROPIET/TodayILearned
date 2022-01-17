import sys
sys.stdin = open('input.txt')

import random

def get_target(now_x, now_y, now_memory, direction):
    now_x = now_x % R
    now_y = now_y % C

    now_command = matrix[now_x][now_y]

    # 방향키인지 체크
    if now_command in direction_code:
        direction_idx = direction_code[now_command]

    elif now_command == '?':
        direction_idx = random.randrange(4)

    elif now_command == '_':
        if now_memory:
            direction_idx = 2
        else:
            direction_idx = 0
    
    elif now_command == '|':
        if now_memory:
            direction_idx = 3
        else:
            direction_idx = 1
    
    elif now_command == '+':
        now_memory += 1
        direction_idx = direction

    elif now_command == '-':
        now_memory -= 1
        direction_idx = direction

    elif now_command == '.':
        direction_idx = direction
    
    elif now_command == '@':
        return True

    else:
        now_memory = int(matrix[now_x][now_y])
        direction_idx = direction

    now_memory = now_memory % 16

    if now_memory in check_matrix[now_x][now_y]:
        return False
    
    check_matrix[now_x][now_y].append(now_memory)
    return get_target(now_x+di[direction_idx], now_y+dj[direction_idx], now_memory, direction_idx)

T = int(input())
for test in range(1, T+1):
    R, C = map(int,input().split())
    matrix = [list(input()) for _ in range(R)]
    check_matrix = [ [list() for _ in range(C)] for _ in range(R)]

    # 이동방향: 우 / 하 / 좌 / 상
    direction_code = {
        '>': 0, 
        'v': 1, 
        '<': 2, 
        '^': 3
    }
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    func_result = get_target(0, 0, 0, 0)

    if func_result:
        print('#{} {}'.format(test, 'YES'))
    else:
        print('#{} {}'.format(test, 'NO'))
