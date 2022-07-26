## Lv.2 가장 큰 정사각형 찾기

https://school.programmers.co.kr/learn/courses/30/lessons/12905

#### 1. 재귀 + 반복문
> - 우측으로 1의 길이 N을 찾아 현재행부터 N행까지의 원소가 모두 1인지 확인하기 
>
> 효율성 테스트 => 시간 초과

#### 2. DP활용해서 풀기
2. DP
> - 참고 강의: https://www.youtube.com/watch?v=9AOMXwNrNpk
> 시간복잡도: O(행 길이 * 열 길이) => O(N * M)

 ```python
    def solution(board):
        answer = 0
        
        N = len(board)
        M = len(board[0])
        
        dp = [[0 for _ in range(M)] for _ in range(N)]
        
        for row in range(N):
            for col in range(M):                
                if board[row][col]:
                    dp[row][col] = min(dp[row-1][col], dp[row-1][col-1], dp[row][col-1]) + 1
                
                if answer < dp[row][col]:
                    answer = dp[row][col]
        return answer ** 2
 ```