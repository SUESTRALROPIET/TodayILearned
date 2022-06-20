## Lv.2  전력망을 둘로 나누기

https://programmers.co.kr/learn/courses/30/lessons/86971

#### 1. wire 없는 경우 모두 탐색 + dfs로 연결된 부분 갯수 세기
> 시간복잡도: O(n)
> 
> - 인접행렬로 연결 여부를 초기화 후, 주어진 전선을 모두 반복하면서 탐색
> 
> - dfs를 활용했지만, 전선 하나를 끊으면 무조건 2부분으로 나눠지는 것을 활용하여 모든 n을 방문하지 않는다


```python
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
```