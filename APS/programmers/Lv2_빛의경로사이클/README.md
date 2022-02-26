## Lv.2 빛의 경로 사이클

https://programmers.co.kr/learn/courses/30/lessons/86052

#### ~~1. dfs로 경로 모두 탐색 후, 경로 길이 반환~~

> - 4 ~ 8  런타임 에러

#### 2. while문으로 재방문할때까지 탐색 후, 경로 길이 반환

```python
def solution(grid):

    # 문자(방향)에 따른 다음 좌표 반환: 각 문자별 리스트는 순서대로 하 / 좌 / 상 / 우
    def get_newposition(code, now_dir, row, col):
        if code == 'S':
            dir_lst = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        elif code == 'L':
            dir_lst = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        else:
            dir_lst = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        ni = row + dir_lst[now_dir][0]
        nj = col + dir_lst[now_dir][1]

        return (ni, nj)

    make_matrix = []    # 입력값 문자별로 리스트에 담기 위해 초기화 
    check = []          # 방문했는지 체크할 리스트 초기화 (예) [[[0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0]]]
    len_row = len(grid) # 행 길이
    for row in grid:
        make_matrix.append(list(row))
        len_col = len(row)  # 열 길이
        check.append([[0]*4 for _ in range(len_col)])
     
    answer = []     # 최종 경로 길이 담을 리스트 초기화

    for row in range(len_row):      # 모든 경우의 수 탐색! (처음에 (0, 0) 위치에서만 탐색해서 틀림)
        for col in range(len_col):
            for dir_idx in range(4):
                route_cnt = 0       # 경로 길이 담을 값 초기화
                while check[row][col][dir_idx] == 0:    # 방문했던 경로 재방문할때까지 반복

                    check[row][col][dir_idx] = 1            # 방문 체크
                    route_cnt += 1                          # 경로 길이 +1

                    ni, nj = get_newposition(make_matrix[row][col], dir_idx, row, col)  # 새로운 좌표값 반환 후 
                    if row > ni:        # 어디서 들어왔는지 체크하여 new_dir 값 반환
                        new_dir = 0
                    elif col > nj:
                        new_dir = 1
                    elif row < ni:
                        new_dir = 2
                    else:
                        new_dir = 3

                    # 새로운 값들로 초기화 후 
                    row = ni
                    col = nj
                    dir_idx = new_dir
                    # 범위에 맞게 값 변환
                    if row < 0:
                        row += len_row
                    elif len_row <= row:
                        row -= len_row
                    elif col < 0:
                        col += len_col
                    elif len_col <= col:
                        col -= len_col

                # 같은 좌표/같은 경로 재방문 후, route_cnt가 1이상이면 answer에 추가
                if route_cnt:
                    answer.append(route_cnt)

    answer.sort()   # 오름차순 정렬
    return answer
```

