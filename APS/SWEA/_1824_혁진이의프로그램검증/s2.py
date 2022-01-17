import sys
sys.stdin = open('input.txt')

def get_target(now_x, now_y, now_memory, direction):
    # 이동방향: 우 / 하 / 좌 / 상
    direction_code = {
        '>': 0,
        'v': 1,
        '<': 2,
        '^': 3
    }
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    now_x = now_x % R
    now_y = now_y % C
    now_memory = now_memory % 16

    if (now_x, now_y, now_memory, direction) in check:
        return
    else:
        check.append((now_x, now_y, now_memory, direction))

    now_command = matrix[now_x][now_y]

    # 방향키인지 체크
    if now_command in direction_code:
        direction_idx = direction_code[now_command]

    elif now_command == '?':
        for k in range(4):
            if get_target(now_x + di[k], now_y + dj[k], now_memory, direction):
                return True
                break
        else:
            return

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
        now_memory = int(now_command)
        direction_idx = direction

    return get_target(now_x + di[direction_idx], now_y + dj[direction_idx], now_memory, direction_idx)



T = int(input())
for test in range(1, T + 1):
    R, C = map(int, input().split())
    matrix = [list(input()) for _ in range(R)]
    check = []
    func_result = False

    func_result = get_target(0, 0, 0, 0)

    if func_result:
        print('#{} {}'.format(test, 'YES'))
    else:
        print('#{} {}'.format(test, 'NO'))



