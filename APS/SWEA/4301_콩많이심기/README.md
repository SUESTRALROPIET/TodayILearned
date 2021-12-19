## 4301_콩 많이 심기

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWLv-yZah48DFAVV&categoryId=AWLv-yZah48DFAVV&categoryType=CODE&problemTitle=4301&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

#### ~~1. 현재 기준! 길이가 2인 곳(상하좌우)을 dfs로 탐색하면서 boolean 값 담기~~

> Runtime error

 ```python
 def get_boolean(row_idx, col_idx, now_status):
     # 우 / 하 / 좌 / 상 으로 row_idx/col_idx와의 길이가 2인 부분 탐색하기
     di = [0, 2, 0, -2]  
     dj = [2, 0, -2, 0]
 
 ...
 ```

#### 2. 현재 기준! 길이가 2인 곳(우측 / 우측하단 / 하단)을 dfs로 탐색하면서 boolean값으로 담기

> 위 방식과 같이 델타이동했을 때와의 차이점
>
> - 배열 (0, 0) 에서 우측 하단으로 이동하기 때문에 
>   - 2번 풀이와 같이 델타이동하면 불필요한 함수(stack)가 쌓이지 않는다.
>   - 1번 풀이와 같이 이동하면, 배열 (0, 0)에서 불필요한 곳(좌측 / 우측)까지 탐색하게 되어 불필요한 stack이 쌓여 Runtime error가 발생한다.

 ```python
 def get_boolean(row_idx, col_idx, now_status):
                     # row_idx / col_idx 기준
     di = [0, 2, 2]  # 우측 2칸 / 우측 2칸 + 아래 2칸 / 아래 2칸
     dj = [2, 2, 0]
 
     for k in range(3):
         ni = row_idx + di[k]
         nj = col_idx + dj[k]
         if (0 <= ni < M and 0 <= nj < N) and matrix[ni][nj] == '#':
             matrix[ni][nj] = not now_status     # True/False 번갈아 담기
             get_boolean(ni, nj, not now_status) # DFS 탐색
             
 T = int(input())
 for test in range(1, T+1):
     N, M = map(int, input().split())
     matrix = [['#'] * N for _ in range(M)]
 
     for row in range(M):
         for col in range(N):
             if matrix[row][col] == '#':     # 아직 탐색하지 않은 곳을 
                 matrix[row][col] = True         # True값으로 담고
                 get_boolean(row, col, True)         # DFS 출발하기
 
 
     result = 0
     for row in range(M):        # True값이 담긴 원소들 합연산으로 결과값 반환하기
         result += sum(matrix[row])  
 
     print('#{} {}'.format(test, result))
 ```

