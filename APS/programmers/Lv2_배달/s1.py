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