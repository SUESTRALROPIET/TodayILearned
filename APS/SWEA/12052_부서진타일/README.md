## 12052_부서진 타일

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXmwOSJaSNIDFARX&categoryId=AXmwOSJaSNIDFARX&categoryType=CODE&problemTitle=12052&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1



#### 1. 부서진 타일의 주변 타일(2x2 범위) 탐색하면서 전체 타일 탐색하기 

```python
def check_tiles(row_idx, col_idx):
    global result
 
    di = [0, 1, 1]  # 오른쪽 / 우측 하단 / 아래쪽 타일
    dj = [1, 1, 0]
 
    for k in range(3):  # 2x2 주변 타일 탐색하면서
        ni = row_idx + di[k]
        nj = col_idx + dj[k]
 
        if not (0 <= ni < N and 0 <= nj < M):   # 범위 밖이면 => result값 'NO' 반환
            result = 'NO'
            return
         
        if matrix[ni][nj] == '.' or check[ni][nj]:  # 부서진 타일이 아니거나 체크한 적 있는 타일이면
            result = 'NO'                               # => result값 'NO' 반환
            return
         
        check[ni][nj] = 1   # 위 조건 모두 통과하면 체크하기! 
 
T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]  # 타일 2차원 배열
    check = [[0] * M for _ in range(N)]         # 체크
 
    result = 'YES'      # result 값 초기화
 
    for row in range(N):
        for col in range(M):
            if matrix[row][col] == '#' and not check[row][col]: # 부서진 타일이면서 체크한 적이 없을 때
                check_tiles(row, col)   # 탐색
 
     
    print('#{} {}'.format(test, result))
```





