import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    R, C = map(int, input().split())
    matrix = [list(input()) for _ in range(R)]
    history = [(0, 0, 0, 0)]
    check = []
    result = 'NO'

    # 이동방향: 우 / 하 / 좌 / 상
    direction_code = {
        '>': 0,
        'v': 1,
        '<': 2,
        '^': 3
    }
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while history:
        now_x, now_y, memory, direction = history.pop()
        now_x = now_x % R
        now_y = now_y % C
        now_memory = memory % 16
        now_command = matrix[now_x][now_y]

        if now_command == '@':
            result = 'YES'
            break

        if (now_x, now_y, now_memory, direction) in check:
            continue

        else:
            check.append((now_x, now_y, now_memory, direction))

        if now_command in direction_code:
            direction_idx = direction_code[now_command]
            history.append((now_x+di[direction_idx], now_y+dj[direction_idx], now_memory, direction_idx))

        elif now_command == '?':
            for k in range(4):
                direction_idx = k
                history.append((now_x+di[direction_idx], now_y+dj[direction_idx], now_memory, direction_idx))

        elif now_command == '_':

            direction_idx = 0 if now_memory == 0 else 2
            history.append((now_x + di[direction_idx], now_y + dj[direction_idx], now_memory, direction_idx))

        elif now_command == '|':
            direction_idx = 1 if now_memory == 0 else 3
            history.append((now_x + di[direction_idx], now_y + dj[direction_idx], now_memory, direction_idx))

        elif now_command == '+':
            history.append((now_x + di[direction], now_y + dj[direction], now_memory+1, direction))

        elif now_command == '-':
            history.append((now_x + di[direction], now_y + dj[direction], now_memory-1, direction))

        elif now_command == '.':
            history.append((now_x + di[direction], now_y + dj[direction], now_memory, direction))

        else:
            history.append((now_x + di[direction], now_y + dj[direction], int(matrix[now_x][now_y]), direction))

    print('#{} {}'.format(test, result))