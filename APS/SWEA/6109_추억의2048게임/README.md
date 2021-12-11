## 6109_추억의 2048게임
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWbrg9uabZsDFAWQ&categoryId=AWbrg9uabZsDFAWQ&categoryType=CODE&problemTitle=%EC%B6%94%EC%96%B5%EC%9D%98+2048%EA%B2%8C%EC%9E%84&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

#### 1. S값에 따라 계산

> - 모두 탐색하면서 값 비교하면서 result 배열에 결과값 기록하기

```python
T = int(input())
for test in range(1, T+1):
    N, S = input().split()
    N = int(N)

    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = [[0]* N for _ in range(N)]

    # S값에 따라 분기처리

    if S == 'up':
        for col in range(N): # col: 0 -> N-1
            store = 0
            result_idx = 0
            for row in range(N):    # row: 0 -> N-1
                if not store:           # 아직 store에 저장된 수가 없으면
                    store = matrix[row][col]    # store에 숫자 기록하기
                    continue
                if not matrix[row][col]:    # 숫자가 0이면 다음 수 탐색
                    continue
                if matrix[row][col] == store:   # store에 담긴 숫자와 같다면
                    result[result_idx][col] = store * 2 # 같은 수 합 (2배값) result 배열에 저장
                    store = 0                           # store는 초기화
                else:                           # store 숫자와 다르다면
                    result[result_idx][col] = store     # store 수 result 배열에 기록하고 
                    store = matrix[row][col]            # store는 해당 원소값으로 대체
                result_idx += 1                 # result 배열 idx값 변경
            if store:                   # 모두 반복 했는데 store값이 0이 아니면 
                result[result_idx][col] = store     # result 배열에 기록

    elif S == 'down':
        for col in range(N):    # col: 0 -> N-1
            store = 0
            result_idx = N-1
            for row in range(N-1, -1, -1):  # row: N-1 -> 0
                if not store:
                    store = matrix[row][col]
                    continue
                if not matrix[row][col]:
                    continue
                if matrix[row][col] == store:
                    result[result_idx][col] = store * 2
                    store = 0
                else:
                    result[result_idx][col] = store
                    store = matrix[row][col]
                result_idx -= 1
            if store:
                result[result_idx][col] = store

    elif S == 'left':
        for row in range(N):    # row: 0 -> N-1
            store = 0
            result_idx = 0
            for col in range(N):    # col: 0 -> N-1
                if not store:
                    store = matrix[row][col]
                    continue
                if not matrix[row][col]:
                    continue
                if matrix[row][col] == store:
                    result[row][result_idx] = store * 2
                    store = 0
                else:
                    result[row][result_idx] = store
                    store = matrix[row][col]
                result_idx += 1
            if store:
                result[row][result_idx] = store
    elif S == 'right':
        for row in range(N):    # row: 0 -> N-1
            store = 0
            result_idx = N-1
            for col in range(N-1, -1, -1):  # col: N-1 -> 0
                if not store:
                    store = matrix[row][col]
                    continue
                if not matrix[row][col]:
                    continue
                if matrix[row][col] == store:
                    result[row][result_idx] = store * 2
                    store = 0
                else:
                    result[row][result_idx] = store
                    store = matrix[row][col]
                result_idx -= 1
            if store:
                result[row][result_idx] = store
     

    print('#{}'. format(test))
    for row_idx in range(N):
        print(*result[row_idx])
```