import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    X, Y, Z, A, B, C, N = map(int, input().split())

    x_lst = [0] * N     # y, z가 0일 때, 나올 수 있는 나머지의 경우의 수 담기 
    y_lst = [0] * N     # x, z가 0일 때, 나올 수 있는 나머지의 경우의 수 담기 
    z_lst = [0] * N     # x, y가 0일 때, 나올 수 있는 나머지의 경우의 수 담기 

    for x in range(X):
        x_lst[abs(x-A) % N] += 1
    for y in range(Y):
        y_lst[abs(y-B) % N] += 1
    for z in range(Z):
        z_lst[abs(z-C) % N] += 1

    xy_lst = [0] * N    # z가 0일때, 나올 수 있는 나머지의 경우의 수
    for x in range(N):
        for y in range(N):
            xy_lst[(x+y) % N] += (x_lst[x] * y_lst[y])

    xyz_lst = [0] * N   # x/y/z 모든 경우의 수 합치기
    for xy in range(N):
        for z in range(N):
            xyz_lst[(xy+z) % N] += (xy_lst[xy] * z_lst[z])

    # print(x_lst, y_lst)
    # print(xy_lst)
    print('#{}'.format(test), *xyz_lst)