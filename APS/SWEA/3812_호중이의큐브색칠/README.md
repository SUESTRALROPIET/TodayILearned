## 3812. 호중이의 큐브색칠

https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AWH0GF0aBNADFAVB&categoryId=AWH0GF0aBNADFAVB&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=6

#### ~~1. 모든 X / Y / Z 탐색하면서 색 값 구하기~~

> - 제한시간 초과

```python
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
```

#### 2. 선 > 면 > 육면체 경우의 수 순서대로 구하기

1. X, Y, Z 각 각에서 나올 수 있는 색 값의 경우의 수 구하기
2. X & Y에서 나올 수 있는 색 값의 경우의 수 구하기
3. X & Y & Z에서 나올 수 있는 색 값의 경우의 수 구하기

```python
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
 
    print('#{}'.format(test), *xyz_lst)
```



