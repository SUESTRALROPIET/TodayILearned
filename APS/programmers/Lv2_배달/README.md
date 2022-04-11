## Lv.2 배달

https://programmers.co.kr/learn/courses/30/lessons/12978

#### 1. 2차원 배열에 거리길이 담고, 갈 수 있는 곳부터 탐색하기(bfs로 풀기)

```python
def solution(N, road, K):
    matrix = [[0] * N for _ in range(N)]

    # matrix에 입력값(최단거리) 채우기
    for ele in road:
        a, b, dist = ele
        if matrix[a-1][b-1] and matrix[a-1][b-1]<= dist:
            continue
        matrix[a-1][b-1] = dist
        matrix[b-1][a-1] = dist
    
    visited = [float('INF')] * N
    stack = [(0, 0)]
    
    # bfs로 갈 수 있는 경로 체크하기
    while stack:
        now, now_dist = stack.pop(0)
        visited[now] = now_dist
        for next_idx in range(N):
            next_dist = matrix[now][next_idx]   # 갈 경로의 거리길이
            new_dist = now_dist + next_dist     # 지금까지 거리길이
            if visited[next_idx] < new_dist:    # 기록된 길이보다 거리가 더 길면
                continue
            if next_dist and new_dist <= K:
                stack.append((next_idx, new_dist))
          
    answer = 0
    for ele in visited:
        if not ele == float('INF'):
            answer += 1

    return answer
```