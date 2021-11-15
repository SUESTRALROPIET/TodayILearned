import sys
sys.stdin = open('input.txt')

# 비트연산으로 표현한 경우의 수      # 각 원소 표현하기
#   [ 3, 2, 1 ]                         #  [ 3, 2, 1 ]
#   [ 2, 1, 0 ]
# 0 : 0  0  0
# 1 : 0  0  1                           # 0 : 0  0  1
# 2 : 0  1  0                           # 1 : 0  1  0
# 3 : 0  1  1
# 4 : 1  0  0                           # 2 : 1  0  0
# 5 : 1  0  1
# 6 : 1  1  0
# 7 : 1  1  1

def dp(now_status):
    # 이미 계산된 경우의 수라면,
    # 더 이상 계산하지 않고 저장된 값 반환하기
    if calculated[now_status]:
        return cnt_list[now_status]

    # 모든 선수가 들어왔으면 1 반환하여 경우의 수 증가시키기
    if now_status == (1 << N) - 1:
        return 1

    calculated[now_status] = True   # now_status일때의 경우의 수 계산하므로 True로 체크
    for next_player in range(N):        # 모든 선수를 반복하면서
        if now_status & (1 << next_player) == 0 and isSatisfied_condition(now_status, next_player):
            # 1. next_player가 아직 포함되지 않은 상태이고
            # 2. next_player가 들어오기 위해 먼저 들어와야하는 선수가 들어온 경우
            cnt_list[now_status] += dp(now_status | (1 << next_player))

    return cnt_list[now_status]

# new_player가 포함되기 전에
# now_status에 new_player보다 먼저 들어와야하는 선수가 존재하는지 검사
def isSatisfied_condition(now_status, new_player):
    for required in required_player_list[new_player]:
        if now_status & (1 << required) == 0:
            return 0
    return 1

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())

    required_player_list = [[] for _ in range(N)]  # 먼저 들어와야 하는 선수 담기
    calculated = [False] * (1 << N)          # 이미 계산한 경우인지 (경우의 수만큼 생성)
    cnt_list = [0] * (1 << N)            # 계산된 결과 저장!   (경우의 수만큼 생성)

    for _ in range(M):
        required_player, player = map(int, input().split())
        required_player_list[player-1].append(required_player-1)    # [[], [0], [0]]

    result = dp(0)  # 아직 아무도 안 들어온 상태에서 경우의 수 체크하기

    print('#{} {}'.format(test, result))


