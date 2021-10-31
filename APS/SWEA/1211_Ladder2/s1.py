import sys
sys.stdin = open('input.txt')

def dfs(start_point, now_x, now_y, cum_V):
    global min_V, result

    # direction = [(1, 0), (0, 1), (0, -1)]   # 하[0] / 우[1] / 좌[2]
    down_x = now_x + 1
    down_y = now_y + 0
    right_x = now_x + 0
    right_y = now_y + 1
    left_x = now_x + 0
    left_y = now_y - 1

    # min_V보다 cum_V가 크면 더이상 계산하지 X
    if min_V < cum_V:
        return

    # 마지막 행에 도달했으면 min_V, result(start_point)값 갱신
    if now_x == 100 - 1:
        min_V = cum_V
        result = start_point
        return

    # 오른쪽 : 유효성 검사 & 방문 체크 & 갈 수 있는지 체크 > 방문 체크 > dfs 재귀
    if 0 <= right_y < 100 and visited[right_x][right_y] == 0 and ladder[right_x][right_y] == 1:
        visited[right_x][right_y] = 1
        dfs(start_point, right_x, right_y, cum_V + 1)

    # 왼쪽 : 유효성 검사 & 방문 체크 & 갈 수 있는지 체크 > 방문 체크 > dfs 재귀
    elif 0 <= left_y < 100 and visited[left_x][left_y] == 0 and ladder[left_x][left_y] == 1:
        visited[left_x][left_y] = 1
        dfs(start_point, left_x, left_y, cum_V + 1)

    # 아래 : 유효성 검사 & 방문 체크 & 갈 수 있는지 체크 > 방문 체크 > dfs 재귀
    elif 0 <= down_x < 100 and visited[down_x][down_y] == 0 and ladder[down_x][down_y] == 1:
        visited[down_x][down_y] = 1
        dfs(start_point, down_x, down_y, cum_V + 1)
    
for _ in range(10):
    test = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    # 출발지 idx 모두 start_list에 담아주기
    start_list = []
    for idx in range(100):
        if ladder[0][idx] == 1:
            start_list.append(idx)

    # 최소값 / result(시작점) 초기화
    min_V = float('INF')
    result = 0

    # 출발할 수 있는 지점 모두 반복하면서 
    for start in start_list:
        visited = [[0] * 100 for _ in range(100)]   # 방문 체크할 2차원 리스트 초기화
        visited[0][start] = 1       # 출발지 방문 체크 후 
        dfs(start, 0, start, 1)     # dfs를 (0, 출발 인덱스)부터 출발! //start는 출발지 idx 기록하기 위해서 추가!
    
    print('#{} {}'.format(test, result))