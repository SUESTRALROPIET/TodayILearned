## 1197. 최소 스패닝 트리 

https://www.acmicpc.net/problem/1197

#### 1. 프림 알고리즘 + heapq
> 시간 복잡도: O(E log V)

```python
import heapq

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

distance = [0 for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]

q = [(0, 1)]

while q:
    cost, now = heapq.heappop(q)
    if visited[now]:
        continue

    visited[now] = True
    distance[now] = cost

    for ele in graph[now]:
        heapq.heappush(q, ele)

print(sum(distance))
```

#### 2. 1번 풀이 + 연결된 노드 기록하기