import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    input_lst = [0] + list(map(int, input().split()))
    result = ''
    
    for _ in range(M):
        code, a, b = map(int, input().split())

        if code == 1:
            input_lst[a] += b
        else:
            result += ' ' + str(sum(input_lst[a:b+1]))

    print('#{}{}'.format(test, result))