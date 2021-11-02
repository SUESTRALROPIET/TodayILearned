## 4613_러시아 국기 같은 깃발

https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AWQl9TIK8qoDFAXj&categoryId=AWQl9TIK8qoDFAXj&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=3
#### 1. 흰 + 파 + 빨의 숫자를 반복문을 통해 구하고 변경횟수 구하기


```python
# line_idx번째 줄에 color로 바꿔야하는 개수 반환
def get_cnt(line_idx, color):
    global temp_cnt
    temp_cnt = 0
    for flag in flag_lines[line_idx]:
        if flag != color:
            temp_cnt += 1
    return temp_cnt

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    flag_lines = [list(input()) for _ in range(N)]

    result = N * M
    for i in range(1, N):           # 흰색이 1줄 이상
        for j in range(1, N):       # 파란색 1줄 이상 
            for k in range(1, N):   # 빨간색 1줄 이상
                if i + j + k == N:      # 흰 + 파 + 빨 모두 합해서 N줄이면
                    cnt = 0                 # 바꿔야하는 횟수 세어보기 
                    for w in range(i):          # 흰색줄에서 바꿔야하는 색 수 
                        cnt += get_cnt(w, 'W')      
                    for b in range(j):          # 파란색줄에서 바꿔야하는 색 수 
                        cnt += get_cnt(i + b, 'B')
                    for r in range(k):          # 빨간색줄에서 바꿔야하는 색 수 
                        cnt += get_cnt(i + j + r, 'R')

                    if cnt < result:    # result값과 비교하여 cnt가 더 작으면 cnt를 result값에 할당
                        result = cnt

    print('#{} {}'.format(test, result))