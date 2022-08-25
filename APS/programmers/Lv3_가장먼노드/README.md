## Lv.3 가장 먼 노드

https://school.programmers.co.kr/learn/courses/30/lessons/49189

#### 1. 그래프(인접리스트) + BFS & deque
> 시간복잡도: O(노드개수 + 간선개수) => O(V + E)

```python
    from collections import deque

    def solution(n, edge):
        answer = 0
        
        graph = [[] for _ in range(n+1)]
        
        for ele in edge:
            fr, to = ele
            graph[fr].append(to)
            graph[to].append(fr)
        
        max_cnt = 0
        visited = [False for _ in range(n+1)]
        visited[1] = True
        q = deque([(1, 0)])
        
        while q:
            node, dist = deque.popleft(q)
            if max_cnt < dist:
                max_cnt = dist
                answer = 1
            elif max_cnt == dist:
                answer += 1
            for next_node in graph[node]:
                if visited[next_node]:
                    continue
                visited[next_node] = True
                q.append((next_node, dist+1))
            
        return answer
```