## Lv.3 퍼즐 조각 채우기

https://school.programmers.co.kr/learn/courses/30/lessons/84021

#### 1. 반복문과 반복문과 반복문...
> 풀이 방법
>
>   1. 좌측 상단과 우측 하단 좌표를 구해 n x m 크기인 직사각형 형태로 퍼즐을 분리해서 배열에 담기
>   2. 배열을 90도씩 회전하면서 XOR(^) 비트연산 하여 검사
>   3. 퍼즐값이 1인 table행렬을 합하여 answer에 더함

> 시간복잡도: O(N^2)
>
> - 두 행렬을 완전탐색하여 구함

 ```python
  def check(board_puzzles, table_puzzles, cnt):   # board_puzzles, B가 서로 대응하는지 확인
      if cnt == 4:
          return False
          
      if len(board_puzzles) != len(table_puzzles):    # 행 길이가 안 맞으면 회전 후, 다시 검사
          return check(board_puzzles, rotate(table_puzzles), cnt+1)

      row = len(board_puzzles)
      col = len(board_puzzles[0])

      for i in range(row):
          for j in range(col):
              if board_puzzles[i][j] ^ table_puzzles[i][j] == 0:  # 서로 같으면 => 퍼즐 안 맞음 ==> 회전 후, 다시 검사
                  return check(board_puzzles, rotate(table_puzzles), cnt+1)
      return True

  def rotate(arr):    # arr을 시계방향으로 90도 회전 (최대 270도까지만!, check함수에서 cnt로 걸러 줌)
      N = len(arr[0])
      M = len(arr)

      matrix = [[0 for _ in range(M)] for _ in range(N)]

      for i in range(N):
          row = M - 1
          for j in range(M):
              matrix[i][j] = arr[row][i]
              row -= 1

      return matrix

  def get_puzzle(matrix, target):    # target과 일치하는 부분에서 퍼즐 범위 담기
      N = len(matrix)
      return_lst = []                             # target에 해당하는 숫자가 있는 부분 담기
      checked = [[False] * N for _ in range(N)]   # 체크했는지 검사
      q = []
      
      for r in range(N):
          for c in range(N):
              if checked[r][c]:               # 체크한 적 있으면 continue
                  continue
              if matrix[r][c] == target:      # 해당 위치가 target 숫자와 동일하면
                  q.append((r, c))   # q에 추가! (좌상단 R, C, 우하단 R, C)
                  min_r = max_r = r                   # 범위를 잡기 위해 min_r, max_r, min_c, max_c 설정
                  min_c = max_c = c
                  while q:
                      now_r, now_c = q.pop()
                      dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]    # 우 / 하 / 좌 / 상
                      for k in range(4):
                          ni = now_r + dir[k][0]
                          nj = now_c + dir[k][1]
                          if not (0 <= ni < N and 0 <= nj < N):   # 유효성 체크
                              continue
                          if checked[ni][nj]:                     # 체크했는지 검사
                              continue
                          if matrix[ni][nj] != target:            # target과 다르면 continue
                              continue
                              
                          checked[ni][nj] = True          # 체크 후, min_r, min_c, max_r, max_c 갱신
                          if ni < min_r:
                              min_r = ni
                          if nj < min_c:
                              min_c = nj
                          if max_r < ni:
                              max_r = ni
                          if max_c < nj:
                              max_c = nj
                          q.append((ni, nj))
                          
                  return_lst.append((min_r, min_c, max_r, max_c))     # 범위(좌측 상단 행, 열, 우측 하단 행, 열) 값 추가
      return return_lst

  def solution(game_board, table):     
      def get_table(position, origin):    # position(좌측상단 행, 열, 우측 하단 행, 열)으로 해당하는 table값 반환하기
          return_list = []
          TR, TC, BR, BC = position
          for ele in origin[TR:BR+1]:
              return_list += [ele[TC:BC+1]]
          return return_list
      
          
      answer = 0 
      board_list = get_puzzle(game_board, 0)
      table_list = get_puzzle(table, 1)

      board_puzzles = []
      table_puzzles = []
      for position in board_list:
          board_puzzles.append(get_table(position, game_board))
      for position in table_list:
          table_puzzles.append(get_table(position, table))
          
      # board_puzzles, table_puzzles 배열에 담긴 도형이 상응하는지 체크
      table_puzzles_checked = [False for _ in range(len(table_puzzles))]      # 체크한 table_puzzles인지 기록
      for board_puzzle in board_puzzles:
          board_row = len(board_puzzle)   # board_puzzle의 행 길이, 열 길이
          board_col = len(board_puzzle[0])
          for idx in range(len(table_puzzles)):
              if table_puzzles_checked[idx]:  # 체크한 table_puzzle인지 확인
                  continue
              table_row = len(table_puzzles[idx])     # table_puzzle 행 길이, 열 길이
              table_col = len(table_puzzles[idx][0])

              # 행/열 길이가 동일한지, 회전시켰을 때 행/열 길이가 동일한지 체크 => 다르면 전혀 안 맞는 퍼즐들
              if (board_row == table_row and board_col == table_col) or (board_row == table_col and board_col == table_row):
                  is_True = check(board_puzzle, table_puzzles[idx], 0)

                  if is_True:     # 서로 맞는 퍼즐이면
                      table_puzzles_checked[idx] = True   # check
                      for k in table_puzzles[idx]:        # table_puzzles에 담긴 1 합하기
                          answer += sum(k)
                      break
              
      return answer
 ```

