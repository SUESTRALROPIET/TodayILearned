import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    sport_list = list(map(int, input().split()))
    person_list = list(map(int, input().split()))

    score_list = [0] * N    # 점수기록 리스트
    result_idx = 0          # 최고점 종목 idx
    max_score = 0           # 최고점

    for person in person_list:
        for idx in range(N):
            if sport_list[idx] <= person:   # 심사위원 최대점수 이하이면
                score_list[idx] += 1            # 점수 기록
                if max_score < score_list[idx]: # 점수와 최고점 비교해서
                    result_idx = idx                # 최고점 종목 idx & 최고점 갱신
                    max_score = score_list[idx]
                break
    
    print('#{} {}'.format(test, result_idx+1))