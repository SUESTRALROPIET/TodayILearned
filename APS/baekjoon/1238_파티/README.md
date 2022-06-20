## 1238 파티

https://www.acmicpc.net/problem/1238

#### 1. 우선순위 큐 사용하기
> 시간복잡도: O(V * E log V)
>
> - 모든 노드로부터 다른 노드까지 얼마나 걸리는지 모두 구하기 때문에 V배 걸릴 것으로 보임

```python
  import heapq

  N, M, X = map(int, input().split())

  path = [[] for _ in range(N + 1)]
  answer = [[float('INF')] * (N + 1) for _ in range(N + 1)]

  for _ in range(M):
      start, end, cost = map(int, input().split())
      path[start].append((cost, end))

  for start_node in range(1, N + 1):
      q = []

      answer[start_node][start_node] = 0
      heapq.heappush(q, (0, start_node))

      while q:
          dist, node = heapq.heappop(q)
          if answer[start_node][node] < dist:
              continue

          for ele in path[node]:
              new_dist = dist + ele[0]
              if new_dist < answer[start_node][ele[1]]:
                  answer[start_node][ele[1]] = new_dist
                  heapq.heappush(q, (new_dist, ele[1]))

  max_num = float('-INF')
  for idx in range(1, N+1):
      cost = answer[idx][X] + answer[X][idx]
      if max_num < cost:
          max_num = cost

  print(max_num)
```
