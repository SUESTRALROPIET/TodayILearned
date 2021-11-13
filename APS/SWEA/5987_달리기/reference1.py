import sys
sys.stdin = open('input.txt')

# n은 N자리의 비트로 각 번째의 선수가 완주했으면 1, 완주하지 않았으면 0을 나타낸다.
def DP(n):
    # 모든 달리기 선수들이 통과한 경우(N개의 1로 이루어진 N개의 비트가 완성된 경우) => 1개의 case 완성
    if n == (1 << N) - 1:
        return 1
    # 현재 완주한 달리기 선수들의 케이스가 이미 나왔던 케이스와 같다면 이후 벌어질 경우의 수들이 같을 것
    # ex. 1 3 2 4 5의 케이스와 1 2 3 5 4의 케이스는 이후의 진행 상황은 결국 같을 것이다.
    if dp[n] != -1:
        return dp[n]
    # 현재에 대한 경우의 수를 0으로 맞춰준다.(이 후의 경우의 수들을 다 더해 나갈 것)
    dp[n] = 0
    for i in range(N):
        # i번째 선수가 아직 들어오지 않은 상태이면서, i의 이전에 들어와야 할 선수들이 모두 들어온 상태면 i가 들어온다.
        if n & (1 << i) == 0 and check(n, i):
            # 현재의 경우의 수에 i번째 선수가 들어온 경우의 수를 더한다.
            dp[n] += DP(n | (1 << i))
    # 작업이 끝나면 현재의 경우의 수를 리턴한다.
    return dp[n]
 
 
def check(n, i):
    # i의 이전에 들어와야 할 선수들 번째의 비트가 모두 1이어야 i가 들어올 수 있는 상태가 된다.
    for f in front[i]:
        if n & (1 << f) == 0:
            return 0
 
    return 1
     
     
for t in range(1, int(input())-1):
    N, M = map(int, input().split())
    front = [[] for _ in range(N)]
    dp = [-1]*(1 << N)
    for _ in range(M):
        x, y = map(int, input().split())
        # 비트 연산에 편하게 맞추기 위해 1번째 선수가 아닌 0번째 선수부터 시작하는 것으로 한다.
        front[y-1].append(x-1)
    # DP(0)은 아무도 통과하지 않은 상태부터 시작하겠다는 것
    print('#%d %d' % (t, DP(0)))    