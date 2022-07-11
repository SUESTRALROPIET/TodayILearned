# BFS(Breadth-First Search) 알고리즘
- 너비 우선 탐색
- 그래프에서 가까운 부분을 우선적으로 탐색하는 알고리즘

## 알고리즘 원리
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리 한다.
3. 2 번 과정을 더 이상 수행할 수 없을 때까지 반복한다.

## 구현하기
1. graph, visited 배열 초기화
    ```python
    graph = []  # 인접 행렬 또는 인접 리스트
    visited = [False] * N
    ```
2. bfs 함수
    ```python
    from collections import deque

    dfe bfs(graph, start, visited):
      queue = deque([start])
      visited[start] = True # 방문처리

      while queue:
        v = queue.popleft() # 원소 하나 뽑기
        print(v, end=" ")

        for i in graph[v]:
          if not visited[i]:
            queue.append(i)
            visited[i] = True
    ```


## 시간 복잡도 공간복잡도
> DFS와 시간복잡도가 동일하다.

| 그래프 구현 방법  | 시간 복잡도 |  
| :--: | :------------------------------------ 
|  인접 행렬  |  O(V^2)  |
|  인접 리스트  |  O(V + E)  |

- 인접 행렬 - 시간 복잡도
  1. 모든 정점 탐색하는 시간복잡도: O(V)
  2. 현재 정점에서 모든 정점 탐색: O(V)
  3. O(V*V) = O(V^2)

- 인접 리스트 - 시간 복잡도
  1. 모든 정점 탐색: O(V)
  2. 현재 정점에 연결된 간선 반복 O(E)
  3. O(V + 2E) => O(V + E)


## 참고 자료
- [이것이 취업을 위한 코딩 테스트다](http://www.yes24.com/Product/Goods/91433923)