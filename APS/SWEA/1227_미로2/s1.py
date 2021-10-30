import sys
sys.stdin = open('input.txt')

def bfs():
    global stack, stack_idx, result

    # stack_idx가 stack 길이보다 작으면 while 이하 명령문 실행
    while stack_idx < len(stack):
        x, y = stack[stack_idx]     # stack 요소 x, y에 할당

        if miro[x][y] == 3:     # 목적에 도착하면 reuslt값 1로 반환 후, 반복문 빠져나오기
            result = 1
            break

        # 우 / 하 / 좌 / 상
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        
        for k in range(4):  # 4방향 모두 검사해서 
            ni = x + di[k]
            nj = y + dj[k]
            
            if not (0 <= ni < 100 and 0 <= nj < 100):   # 유효성 검사
                continue

            if miro[ni][nj] == 1 or visited[ni][nj] == 1:   # 벽이거나 방문한 적이 있으면 다른 곳 탐색
                continue

            visited[ni][nj] = 1     # 위 조건을 통과하면 방문체크 후, 
            stack.append((ni, nj))  # 가능한 곳 stack에 추가
        
        stack_idx += 1  # 다음 stack 탐색하기
        
    
for _ in range(1, 11):
    test = int(input())
    miro = [list(map(int, input())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    
    # 시작점 / 목적지 찾기
    for x in range(100):
        for y in range(100):
            if miro[x][y] == 2:
                start_x, start_y = x, y
                break

    visited[start_x][start_y] = 1   # 출발지 방문체크
    stack = [(start_x, start_y)]    # stack에 출발지 담기
    stack_idx = 0           # stack_idx 0으로 초기화
    result = 0              # result : 목적지까지 길이 있으면 1/ 없으면 0

    # bfs 시작
    bfs()   

    print('#{} {}'.format(test, result))


    