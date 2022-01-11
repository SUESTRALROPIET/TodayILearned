## 3064_Binary Indexed Tree
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_Wo_Sa6UEDFAXw&categoryId=AV_Wo_Sa6UEDFAXw&categoryType=CODE&problemTitle=3064&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

### Binary Indexed Tree 참고 자료
1. 펜윅 트리(Fenwick Tree, Binary Indexed Tree, BIT)
    https://greeksharifa.github.io/algorithm%20&%20data%20structure/2018/07/09/algorithm-fenwick-tree/
2. 자료구조: 바이너리 인덱스 트리(Binary Indexed Tree, BIT, 펜윅 트리) 10분 정복
    https://www.youtube.com/watch?v=fg2iGP4e2mc
3. 자료구조 이진인덱스트리 (1/2)
    https://www.youtube.com/watch?v=hUjaxK9zx5M

#### 1. ~~단순하게 풀어보기~~
> 당연히 시간초과가 됐다.
```python
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
```

#### 2. ~~BIT 개념 활용하기~~
> 시간초과 원인: 결과값을 문자열로 변환후 result 문자열에 누적
```python
...
        else:
            result += ' ' + str(cumulativa_sum(b) - cumulativa_sum(a-1))

    print('#{}{}'.format(test, result))
```
#### 3. BIT 개념 활용하기
```python
def add_num(start_idx, add_value):          # start_idx가 영향을 주는 idx에 모두 add_value 더하기
    while start_idx < N+1:                              # start_idx: start_idx -> N
        binary_indexed_tree[start_idx] += add_value
        start_idx += (start_idx & -start_idx)           # 마지막 비트가 1인 값 구하기

def cumulativa_sum(idx):                    # 1 ~ idx까지의 누적합 구하기
    cum_sum = 0
    while 0 < idx:
        cum_sum += binary_indexed_tree[idx]
        idx -= (idx & -idx)                             # 마지막 비트가 1인 값 구하기
    return cum_sum

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    input_num = [0] + list(map(int, input().split()))       # 입력받은 숫자들
    binary_indexed_tree = [0] * (N+1)                       # BIT를 적용해서 입력값을 담을 리스트

    results = []        # 결과값을 리스트에 담기

    for bit_idx in range(1, N + 1):         # bit_idx: 1 -> N
        add_num(bit_idx, input_num[bit_idx])

    for _ in range(M):
        code, a, b = map(int, input().split())
        if code == 1:
            add_num(a, b)
        else:
            results.append(cumulativa_sum(b) - cumulativa_sum(a - 1))

    print('#{}'.format(test), end=' ')
    print(*results)
```