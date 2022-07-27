## Lv.3 정수삼각형

https://school.programmers.co.kr/learn/courses/30/lessons/43105

#### 1. 반복문 + dp 테이블 활용
> 시간복잡도: O(N * N+1) => O(N^2)

 ```python
    def solution(triangle):    
        N = len(triangle)

        dp = []
        for k in range(1, N+1):     # dp 테이블 초기화
            dp.append([0] * k)
        
        dp[0][0] = triangle[0][0]   # 첫 행값 초기화
        
        for row in range(1, N):
            for col in range(row+1):
                now_num = triangle[row][col]
                if col == 0:
                    now_num += dp[row-1][0]
                elif col == row:
                    now_num += dp[row-1][row-1]
                else:
                    now_num += max(dp[row-1][col-1], dp[row-1][col])         
                        
                dp[row][col] = now_num
                
        return max(dp[N-1])
 ```