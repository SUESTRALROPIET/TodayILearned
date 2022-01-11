import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N = int(input())            # 주어진 값에서 2단계 전을 예상해서 빼 나가는 것이 핵심!

    while 3 < N:
        N = N//2 + 1
        N = N//2 - 1

    if N == 1:
        result = 'Bob'
    else:
        result = 'Alice'

    print('#{} {}'.format(test, result))