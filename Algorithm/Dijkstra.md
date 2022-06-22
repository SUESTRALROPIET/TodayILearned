# 다익스트라(Dijkstra) 알고리즘
가중치가 있는 그래프에서 특정 정점으로부터 모든 정점으로 가는 최단 거리를 구할 수 있는 알고리즘

## 알고리즘 원리
> [알고리즘 동작과정 보기](https://www.101computing.net/dijkstras-shortest-path-algorithm/)

1. 값을 기록할 배열을 초기화한다.
  - 노드 방문 여부를 체크할 배열
  - 최단 거리를 기록할 배열
  - *최단 경로를 기록할 배열(최단 경로를 구할 때 필요함)*
2. 시작 노드의 최단거리를 0으로 기록하고, 방문기록을 한다.
3. 시작 노드와 연결된 노드들을 탐색하며 최단 거리를 갱신한다. 
4. 방문하지 않은 노드 중 거리가 가장 짧은 노드를 찾는다.
5. 방문기록을 하고, **해당 노드를 거쳐 다른 노드로 가는 거리**와 **최단 거리 테이블 값**을 비교하여 최단 거리 테이블을 갱신한다.
6. 모든 노드를 방문할 때까지 4~5번을 반복한다.

## 구현하기
> 아래 두 방식은 `알고리즘 원리 4번`을 구현하는 과정에서 시간복잡도 차이가 있다.

### 1. 단순 배열로 구현하기
> `n`: 노드 개수
> `m`: 간선 개수
> `start`: 시작 노드

1. 배열 초기화 및 간선정보 입력
```python
  # 노드(index)에 연결된 간선 정보: (연결된 노드번호, 거리)
  graph = [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)]...]
  visited = [False] * (n+1) # 방문체크
  distance = [float('INF')] * (n+1) # 최단거리 배열
```
2. 시작 노드의 최단거리를 0으로 기록하고, 방문기록을 한다.
```python
  distance[start] = 0
  visited[start] = True
```
3. 시작 노드와 연결된 노드들을 탐색하며 최단 거리를 갱신한다. 
```python
  for ele in graph[start]:
    distance[ele[0]] = ele[1]
```
4. 방문하지 않은 노드 중 거리가 가장 짧은 노드를 찾는다.
```python
  def get_smallest_node():
    min_value = float('INF')
    index = 0
    for node in range(1, n+1):
      if distance[node] < min_value and not visited[node]:
        min_value = distance[node]
        index = node
    return index
```
5. 방문기록을 하고, <u>해당 노드를 거쳐 다른 노드로 가는 거리</u>와 <u>최단 거리 테이블 값</u>을 비교하여 최단 거리 테이블을 갱신한다.
```python
  for _ in range(n-1):
    now = get_smallest_node()
    visited[now] = True
    for ele in graph[now]:
      new_distance = distance[now] + ele[1]
      if new_distance < distance[ele[0]]:
        distance[ele[0]] = new_distance
```

### 2. 우선순위 큐(힙 자료구조)로 구현하기
> **우선순위 큐**
> - 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
> - (a, b)로 묶어서 우선순위 큐 자료구조에 넣으면, 첫 번째 원소 a 기준으로 우선순위를 설정한다.
>   - 최소 힙: 값이 낮은 데이터가 먼저 삭제
>   - 최대 힙: 값이 큰 데이터가 먼저 삭제
> - 다익스트라 알고리즘에서는 비용이 적은 노드를 우선하여 방문하기 때문에 최소 힙 구조를 기반으로 우선순위 큐 라이브러리를 사용하면 적합하다.
>   - python 라이브러리에서는 기본적으로 **최소 힙** 구조를 이용하는데, 언어마다 라이브러리의 자료구조가 조금씩 다르니 사용하기 전에 확인해야한다. 

1 ~ 3. 단순 배열로 구현하는 방법과 유사

4 ~ 5. 거리가 가장 짧은 노드를 우선순위 큐에서 꺼내, 비교 후 최단 거리 테이블을 갱신한다.
```python
  import heapq

  q = []
  heapq.heappush(q, (0, start))

  while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
      continue
    for ele in graph[now]:
      new_distance = dist + ele[1]
      if new_distance < distance[ele[0]]:
        distance[ele[0]] = new_distance
        heapq.heappush(q, (new_distance, ele[0]))
```

## 시간 복잡도 공간복잡도
> - V: 정점/노드 개수
> - E: 간선 개수

| 구현 방법  | 시간 복잡도 | 공간 복잡도 | 
| :--: | :------------------------------------ | :-------: | 
|  단순 배열  |  O(V^2)  |  O(V+E)  |
|  우선순위 큐  |  O(E logV)  |  O(V+E)  |

-  단순 배열 - 시간 복잡도
    - 노드 개수만큼 O(V)번에 걸쳐 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야하고
    - 현재 노드와 연결된 노드를 매번 일일이 확인해야하기 때문
- 우선순위 큐 - 시간 복잡도
    - 한 번 처리된 노드는 더 이상 처리되지 않기 때문에 노드의 개수 V번 이상 반복되지 않는다.
    - 또한 V번 반복될 때 자신과 연결된 간선들을 모두 확인하기 때문에 이때 최대 간선 개수인 E만큼 연산이 수행될 수 있다.

## 활용 문제
1. [SWEA 5250. [파이썬 S/W 문제해결 구현 7 - 최소 비용]
2. [SWEA 5251. [파이썬 S/W 문제해결 구현 7 - 최소 이동 거리]
3. [백준 1238. 파티](https://www.acmicpc.net/problem/1238)
4. [백준 9376. 탈옥](https://www.acmicpc.net/problem/9376)
5. [백준 5719. 거의 최단 경로](https://www.acmicpc.net/problem/5719)
6. [백준 1854. K번째 최단경로 찾기](https://www.acmicpc.net/problem/1854)

## 관련 기술면접 질문
1. 다익스트라 알고리즘이란?
    <details>
    <summary>답변</summary>
    <p>
      특정 노드에서 출발하여 다른 노드로 가는 각각의 최단 거리를 구할 수 있는 알고리즘입니다. 매번 가장 비용이 적은 노드를 선택해서 해당 노드와 연결된 다른 노드를 방문해 거리를 비교 후 갱신해주는 방식이며, 우선순위 큐를 활용해 구현할 수도 있습니다.
      다익스트라 알고리즘의 시간 복잡도는 O(V^2)이지만, 우선순위 큐를 활용해 구현하면 시간 복잡도는 O(ElogV)로 줄일 수 있습니다.
    </p>
    </details>
2. 다익스트라 알고리즘을 우선순위 큐로 사용했을 때의 이점
    <details>
    <summary>답변</summary>
    <p>
      단순 배열로 구현된 다익스트라 알고리즘의 시간 복잡도는 O(V^2)이지만, 우선순위 큐를 활용해 구현하면 시간 복잡도는 O(ElogV)로 줄일 수 있습니다.
      최소 힙으로 구현된 우선순위 큐를 활용하면, 매번 최단 거리가 가장 짧은 노드를 선형 탐색해 찾을 필요가 없기 때문입니다.
    </p>
    </details>
3. 다익스트라 알고리즘이 쓰이는 상황
    <details>
    <summary>답변</summary>
    <p>
      최단 거리와 최단 경로를 구할 수 있기 때문에 GPS 소프트웨어의 기본 알고리즘으로 채택되고 있다고 알고 있습니다.
    </p>
    </details>
4. BFS와 다익스트라 알고리즘의 차이
    <details>
    <summary>답변</summary>
    <p>
      가중치가 없는 그래프에는 BFS를, 가중치가 있는 그래프에는 다익스트라 알고리즘을 적용하는 것이 적합합니다.
      BFS는 가까운 정점부터 방문하지만, 다익스트라 알고리즘은 비용이 적은 정점부터 방문하며 최단 거리를 기록하기 때문입니다.
    </p>
    </details>
5. 다익스트라/벨만-포드/플로이드-워셜 알고리즘의 차이
    <details>
    <summary>답변</summary>
    <p>
    
      1. 다익스트라 알고리즘
          - 한 정점으로부터 다른 모드 정점으로의 최단 거리를 구하는 알고리즘
          - 모든 간선의 가중치가 음의 값이 없을 때만 정상적으로 동작
          - 음의 가중치가 있는 경우 무한히 사이클을 돌며 거리가 작아지기 때문
          - 시간복잡도: O(E logV)

      2. 벨만-포드 알고리즘
          - 한 정점으로부터 다른 모드 정점으로의 최단 거리를 구하는 알고리즘
          - 음의 가중치를 포함하는 그래프에서 최단 경로를 구함
          - 동적 계획법(DP)이 적용됨
          - 벨만포드는 다익스트라에 비해 많은 시간이 소요됨
          - 시간복잡도: O(VE)

      3. 플로이드-워셜 알고리즘
          - 가능한 모든 정점간의 최단거리를 구하는 알고리즘
          - 시간복잡도: O(V^3)

    </p>
    </details>

## 참고 자료
- [누구나 자료구조와 알고리즘](http://www.yes24.com/Product/Goods/61941073)
- [최단경로 알고리즘(1) - 다익스트라 알고리즘](https://sohyunwriter.tistory.com/39?category=892942)
- [핵심 자료구조 - 그래프 : 최단 경로 : ① : BFS, 다익스트라](https://velog.io/@kasterra/%ED%95%B5%EC%8B%AC-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%B5%9C%EB%8B%A8-%EA%B2%BD%EB%A1%9C-%ED%83%90%EC%83%89)
- [[최단 경로 알고리즘 문제 모음] 다익스트라, 벨만-포드, 플로이드-와샬 (Dijkstra, Bellman-Ford, Floyd-Warshall)](https://everenew.tistory.com/158)
