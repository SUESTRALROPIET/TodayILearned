## 1260. DFS와 BFS

https://www.acmicpc.net/problem/1260

#### 1. DFS & BFS (w.인접리스트)
> 시간 복잡도: O(N+E)

```python
def DFS(num):
    if visited[num]:
        return
    visited[num] = 1
    print(num, end = " ")
    for next in sorted(edges[num]):
        DFS(next)

def BFS(q):
    while q:
        now = q.pop(0)
        if visited[now]:
            continue
        visited[now] = 1
        print(now, end = " ")

        q += sorted(edges[now])

N, M, V = map(int, input().split())
edges = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    edges[start].append(end)
    edges[end].append(start)

visited = [0] * (N + 1)
DFS(V)

print()

visited = [0] * (N + 1)
BFS([V])
```
