## 1922. 네트워크 연결

https://www.acmicpc.net/problem/1922

#### 1. 프림 알고리즘 + heapq
> 시간 복잡도: O(E log V)

```python
import heapq

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
distance = [0 for _ in range(N + 1)]

M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

q = [(0, 1)]
while q:
    val, node = heapq.heappop(q)

    if visited[node]:
        continue

    visited[node] = True
    distance[node] = val

    for ele in graph[node]:
        if visited[ele[1]]:
            continue
        heapq.heappush(q, ele)

print(sum(distance))
```
