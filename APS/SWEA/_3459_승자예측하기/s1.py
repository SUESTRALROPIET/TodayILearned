import sys
sys.stdin = open('input.txt')

# 48479개 맞음

T = int(input())
for test in range(1, T+1):
    N = int(input())

    now_num = 1
    cnt = 0

    while now_num <= N:
        cnt += 1

        if 2 ** (cnt+1) <= N < 2 ** (cnt+2):
            now_num = (now_num * 2) + 1
        else:
            now_num *= 2

    if (cnt-1) % 2:
        winner = 'Alice'
    else:
        winner = 'Bob'

    print('#{} {}'.format(test, winner))