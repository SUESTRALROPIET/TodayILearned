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