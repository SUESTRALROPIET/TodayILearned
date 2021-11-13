import sys
sys.stdin = open('input.txt')

def get_order(k):
    if k == N:
        check_valid(player_list)
    
    for h in range(k, N):
        player_list[k], player_list[h] = player_list[h], player_list[k]
        get_order(k+1)
        player_list[k], player_list[h] = player_list[h], player_list[k]

def check_valid(per_list):
    global cnt
    for condition in condition_list:
        a, b = condition
        if not per_list[a-1] < per_list[b-1]:
            return
    cnt += 1

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())

    player_list = [ i for i in range(1, N+1) ]
    condition_list = [list(map(int, input().split())) for _ in range(M)]
    cnt = 0

    get_order(0)

    print('#{} {}'.format(test, cnt))