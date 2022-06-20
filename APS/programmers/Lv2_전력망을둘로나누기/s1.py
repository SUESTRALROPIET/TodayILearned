def solution(n, wires):
    answer = n

    def dfs(now, cnt):  # dfs로 연결된 갯수 확인하기
        visited[now] = 1
        for next_node in range(1, n+1):
            if visited[next_node]:
                continue
            if container[now][next_node] == 0:
                continue
            dfs(next_node, cnt+1)
        return

    # container에 그래프 초기화
    container = [[0] * (n + 1) for _ in range(n + 1)]
    for wire in wires:
        a, b = wire
        container[a][b] = container[b][a] = 1
    
    # wire 하나씩 끊어가며 탐색
    for wire in wires:
        a, b = wire
        container[a][b] = container[b][a] = 0
        
        visited = [0] * (n + 1)
        dfs(1, 0)
        
        cnt = sum(visited)
        result = abs((n - cnt) - cnt)   # 무조건 2부분으로 나눠지기 때문에 차이 계산
        if result < answer:
            answer = result
        
        container[a][b] = container[b][a] = 1   # 끊은 부분 원상복구
            
    return answer