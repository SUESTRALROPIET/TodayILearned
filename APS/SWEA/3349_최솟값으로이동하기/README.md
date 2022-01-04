## 3349_최솟값으로 이동하기

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWDTN0cKr1oDFAWD&categoryId=AWDTN0cKr1oDFAWD&categoryType=CODE&problemTitle=3349&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1



#### ~~1. 델타이동 + dfs + visited 배열로 풀기~~

> 제한시간 초과

```python
def get_distance(now_x, now_y, target_x, target_y, cnt):
    global part_result

    if part_result <= cnt:
        return

    if now_x == target_x and now_y == target_y:
        if cnt < part_result:
            part_result = cnt
        return
    
    di = [-1, 1, 0, 1, 0, -1]
    dj = [-1, 1, 1, 0, -1, 0]

    for k in range(6):
        ni = now_x + di[k]
        nj = now_y + dj[k]
        
        if not (0 < ni <= W and 0 < nj <= H):
            continue

        if visited[ni][nj]:
            continue
        
        visited[ni][nj] = 1
        get_distance(ni, nj, target_x, target_y, cnt+1)
        visited[ni][nj] = 0


T = int(input())
for test in range(1, T+1):
    W, H, N = map(int, input().split())

    result = 0

    start_x, start_y = map(int, input().split())

    for _ in range(N-1):
        new_x, new_y = map(int, input().split())
        part_result = W * H

        visited = [[0] * (H+1) for _ in range(W+1)]
        
        visited[start_x][start_y] = 1
        get_distance(start_x, start_y, new_x, new_y, 0)

        start_x, start_y = new_x, new_y
        result += part_result

    print('#{} {}'.format(test, result))

```

#### 2. 인덱스 값을 비교하여 북동방향 우선계산 후 동서남북 거리 계산하기


```python
T = int(input())
for test in range(1, T+1):
    W, H, N = map(int, input().split())
    result = 0

    start_x, start_y = map(int, input().split())        # 시작 x, y

    for _ in range(N-1):
        target_x, target_y = map(int, input().split())  # 목표 x, y
        steps = 0                                       # 북동방향으로 갈 수 있는 경우 => (i, j)와 (i - 1, j - 1) or (i, j)와 (i + 1, j + 1)
        
        if start_x < target_x and start_y < target_y:   # steps 값이 양수
            steps = min(abs(start_x - target_x), abs(start_y - target_y))
            start_x += steps                                    # 시작 x, y 값 북동방향으로 최대한 옮기기
            start_y += steps
        elif start_x > target_x and start_y > target_y: # steps 값이 음수
            steps = min(abs(start_x - target_x), abs(start_y - target_y))
            start_x -= steps
            start_y -= steps

        result += abs(start_x - target_x) + abs(start_y - target_y) + steps # 동서남북 방향으로 거리 계산하기

        start_x, start_y = target_x, target_y

    print('#{} {}'.format(test, result))
```
