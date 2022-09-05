## Lv.3 섬 연결하기

https://school.programmers.co.kr/learn/courses/30/lessons/42861

#### 1. 프림 알고리즘
> - 시간복잡도: O(V**2)

```python
  def solution(n, costs):   
      graph = [[] for _ in range(n)]
      dist = [float('INF') for _ in range(n)]
      visited = [False for _ in range(n)]
      
      for cost in costs:
          fr, to, val = cost
          graph[fr].append((to, val))
          graph[to].append((fr, val))
      
      dist[0] = 0
      
      for _ in range(n):
          min_node = -1
          min_val = float('INF')
          
          for node in range(n):
              if visited[node]:
                  continue
              if dist[node] < min_val:
                  min_val = dist[node]
                  min_node = node

          visited[min_node] = True

          for new_node, val in graph[min_node]:
              if visited[new_node]:
                  continue
              if val < dist[new_node]:
                  dist[new_node] = val

      return sum(dist)
```

#### 2. 프림 알고리즘 (w. heapq)
> - 시간복잡도: O(E log V)

```python
  import heapq

  def solution(n, costs):   
      graph = [[] for _ in range(n)]
      for fr, to, val in costs:
          graph[fr].append((to, val))
          graph[to].append((fr, val))
      
      dist = [-1 for _ in range(n)]
      visited = [False for _ in range(n)]
      q = [(0, 0)]
      
      while q:
          val, now_node = heapq.heappop(q)
          if visited[now_node]:
              continue
          visited[now_node] = True
          dist[now_node] = val
          
          for next_node, val in graph[now_node]:
              if visited[next_node]:
                  continue
              heapq.heappush(q, (val, next_node))
      
      return sum(dist)
```