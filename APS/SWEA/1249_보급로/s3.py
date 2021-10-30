import sys
sys.stdin = open('input.txt')

def get_target():
    while route_list:   # 경로가 남아있을 때까지 반복
        now_x, now_y = route_list.pop(0)    # 경로 첫번째 값 pop

        # 우 / 하 / 좌 / 상
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]

        for k in range(4):  # 4방향 모두 탐색
            ni = now_x + di[k]
            nj = now_y + dj[k]

            if not (0 <= ni < N and 0 <= nj < N):   # 유효성 검사
                continue

            # 현재 값 + 새 위치 값이 새 위치 값보다 작으면 => 최소값으로 갱신 and route_list에 추가!
            if result_list[now_x][now_y] + matrix[ni][nj] < result_list[ni][nj]:
                result_list[ni][nj] = result_list[now_x][now_y] + matrix[ni][nj]
                route_list.append((ni, nj))

T = int(input())
for test in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]    # 입력값
    result_list = [[float('INF')] * N for _ in range(N)]    # 최소값 담기
    result_list[0][0] = 0       # 시작점 최소값 초기화
    route_list = [(0, 0)]       # 경로 담을 route_list 선언

    get_target()    # 함수 시작!

    print('#{} {}'.format(test, result_list[N-1][N-1]))
