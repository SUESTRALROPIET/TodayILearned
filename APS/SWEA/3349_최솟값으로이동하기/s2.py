import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    W, H, N = map(int, input().split())
    result = 0

    start_x, start_y = map(int, input().split())        # 시작 x, y

    for _ in range(N-1):
        target_x, target_y = map(int, input().split())  # 목표 x, y
        steps = 0                                       # 북동방향으로 갈 수 있는 경우 => (i, j)와 (i - 1, j - 1) or (i, j)와 (i + 1, j + 1)
        
        if start_x < target_x and start_y < target_y:   # steps 값이 양수
            steps = min(abs(start_x - target_x), abs(start_y - target_y))
            start_x += steps                                    # 시작 x, y 값 북동방향으로 최대한 옮기기
            start_y += steps
        elif start_x > target_x and start_y > target_y: # steps 값이 음수
            steps = min(abs(start_x - target_x), abs(start_y - target_y))
            start_x -= steps
            start_y -= steps

        result += abs(start_x - target_x) + abs(start_y - target_y) + steps # 동서남북 방향으로 거리 계산하기

        start_x, start_y = target_x, target_y

    print('#{} {}'.format(test, result))