import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    checked = [[0] * N for _ in range(N)]

    cnt = 0
    result_list = []

    # 처음부터 반복하면서
    for i in range(N):
        for j in range(N):
            if matrix[i][j] and not checked[i][j]:  # 화학물질이 있고 체크 안된 곳이면
                checked[i][j] = 1                       # 체크

                # 0 만날때까지 행 인덱스 증가시키면서 탐색
                k = i + 1
                h = j
                while matrix[k][h] and not checked[k][h]:
                    checked[k][h] = 1
                    k += 1
                end_row = k-1

                # 0 만날때까지 열 인덱스 증가시키면서 탐색
                k = i
                h = j + 1
                while matrix[k][h] and not checked[k][h]:
                    checked[k][h] = 1
                    h += 1
                end_col = h-1

                # 박스 내 모두 체크하기
                for row in range(i, end_row+1):
                    for col in range(j, end_col+1):
                        checked[row][col] = 1

                # (행크기, 열크기, 행 * 열) 값 result_list에 추가하기
                result_list.append((end_row + 1 - i, end_col + 1 - j, (end_row + 1 - i) * (end_col + 1 - j)))

                # 사각형 개수 세기
                cnt += 1

    # 행*열 기준 > 행크기 기준으로 정렬하기
    result_list.sort(key=lambda x: (x[2], x[0]))

    # 결과값 print
    print('#{} {}'.format(test, cnt), end=" ")
    for result in result_list:
        print(*result[0:2], end=" ")
    print()
