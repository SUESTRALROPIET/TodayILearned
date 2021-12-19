## 1686_파핑파핑 지뢰찾기

https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV5LwsHaD1MDFAXc&categoryId=AV5LwsHaD1MDFAXc&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=2

#### ~~1. dfs로 주변을 연쇄적으로 터뜨리기 (fail)~~

> - dfs로 연쇄적으로 터뜨리긴 했으나 최소한 몇 번 클릭해야하는지 구하지 못했다.


```python
import sys
sys.stdin = open('input.txt')

def dfs(now_x, now_y, cnt):
    visited[now_x][now_y] = 1

    di = [-1, -1, -1, 0, 1, 1, 1, 0]
    dj = [-1, 0, 1, 1, 1, 0, -1, -1]

    now_cnt = 0
    for k in range(8):
        ni = now_x + di[k]
        nj = now_y + dj[k]
        if not (0 <= ni < N and 0 <= nj < N):
            continue
        if visited[ni][nj] or matrix[ni][nj] == '.':
            continue
        if matrix[ni][nj] == '*':
            now_cnt += 1

    matrix[now_x][now_y] = now_cnt
    if matrix[now_x][now_y] == 0:
        for k in range(8):
            ni = now_x + di[k]
            nj = now_y + dj[k]
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if visited[ni][nj]:
                continue
            dfs(ni, nj, cnt+1)

T = int(input())
for test in range(1, 2):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '.':
                dfs(i, j, 1)

    print(matrix)