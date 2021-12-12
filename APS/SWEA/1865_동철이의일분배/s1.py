import sys
sys.stdin = open('input.txt')

def get_work(person_idx, now_result):
    global max_result

    if now_result <= max_result:    # 현재 일률 결과값이 max_result보다 작거나 같으면
        return                          # 탐색 중지

    if person_idx == N:             # 모든 직원에게 일 배분이 끝나면
        if max_result < now_result:     # 현재 일률 & max_result 비교해서
            max_result = now_result         # max_result 값 반환하기
        return

    for workd_idx in range(N):      # 일 리스트 전체를 반복하면서
        if finished_work[workd_idx]:    # 이미 배정된 일이면 continue
            continue
        finished_work[workd_idx] = 1    # 해당 업무 배정됨 체크!
        get_work(person_idx+1, now_result*matrix[person_idx][workd_idx]*0.01)   # 직원 수 1 추가 / 현재 일률 * 해당하는 일률 * 0.01 
        finished_work[workd_idx] = 0    # 해당 업무 배정됨 체크 풀기!

T = int(input())
for test in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    finished_work = [0] * N     # 배정된 일인지 체크하기
    max_result = float('-INF')  # 일률 최대값

    get_work(0, 1)  # 0번째 사람부터 시작 / 현재 일률 1로 초기화

    print('#{} {:6f}'.format(test, max_result*100))