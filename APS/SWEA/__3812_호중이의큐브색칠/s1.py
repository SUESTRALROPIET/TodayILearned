import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    X, Y, Z, A, B, C, N = map(int, input().split())

    max_sum = X + Y + Z - 3
    check_lst = [0] * N

    if N == 1:
        check_lst[0] = X * Y * Z
    
    else:
        for x in range(X):
            for y in range(Y):
                for z in range(Z):
                    idx = (abs(x - A) + abs(y - B) + abs(z - C)) % N
                    check_lst[idx] += 1

    print('#{}'.format(test), *check_lst)

    