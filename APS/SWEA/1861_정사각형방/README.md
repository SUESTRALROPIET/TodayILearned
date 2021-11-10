## 1861_정사각형방
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LtJYKDzsDFAXc&categoryId=AV5LtJYKDzsDFAXc&categoryType=CODE&problemTitle=1861&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

#### 1.DFS로 풀기
> Pycharm에서는 시간초과, SWEA는 통과
```python
def dfs(start_i, start_j, now_i, now_j, cnt):
    global result_cnt, result_list

    # 횟수 / 횟수와 동일한 결과를 같는 출발지점 수 기록하기
    if result_cnt < cnt:
        result_list = []
        result_cnt = cnt
        result_list.append(matrix[start_i][start_j])
    elif result_cnt == cnt:
        result_list.append(matrix[start_i][start_j])

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for k in range(4):
        ni = now_i + di[k]
        nj = now_j + dj[k]
        if not (0 <= ni < N and 0 <= nj < N):
            continue
        if matrix[now_i][now_j] + 1 == matrix[ni][nj]:  # 1보다 큰 방으로만 이동
            dfs(start_i, start_j, ni, nj, cnt+1)

T = int(input())
for test in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result_cnt = 0
    result_list = []

    for i in range(N):
        for j in range(N):
            dfs(i, j, i, j, 1)

    print('#{} {} {}'.format(test, min(result_list), result_cnt))
```

#### 2. BFS로 풀기?
```python

```
