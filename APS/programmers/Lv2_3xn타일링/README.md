## Lv.2 3 x n 타일링

https://programmers.co.kr/learn/courses/30/lessons/12902#qna

#### 1. 피보나치수열 특징을 찾아 풀기 + DP
> 참고 사이트: https://yabmoons.tistory.com/471
>
> 시간 복잡도: O(n^2)
> - dp에 값을 저장해놓기 위해 이중 for문을 실행하면, 2500^2 의 
시간이 걸린다.

```python
dp = [0] * 5001
dp[0] = 1
dp[2] = 3
for i in range(4, 5000+1, 2):
    dp[i] = dp[i - 2] * dp[2]
    for j in range(i-4, -1, -2):
        dp[i] += dp[j] * 2

    dp[i] %= 1000000007
    
def solution(n):     
    if n % 2:
        return 0

    return dp[n]
```
