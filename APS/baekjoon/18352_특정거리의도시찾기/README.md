## 18352. 특정 거리의 도시 찾기

https://www.acmicpc.net/problem/18352

#### 1. BFS (w.인접리스트)
> 시간 복잡도: O(N+E)
> - sys.stdin.readline 으로 시간초과 해결
> - 정답 sort해서 오름차순으로 출력

```python
import sys
from collections import deque

def BFS(q):
    q = deque(q)

    while q:
        now, dist = deque.popleft(q)
        if visited[now]:
            continue

        visited[now] = 1
        if dist == K:
            answer.append(now)

        for next_node in edges[now]:
            if visited[next_node]:
                continue
            deque.append(q, (next_node, dist+1))

N, M, K, X = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    edges[start].append(end)

visited = [0] * (N + 1)
answer = []
BFS([(X, 0)])

if answer:
    for ele in sorted(answer):
        print(ele)
else:
    print(-1)
```
