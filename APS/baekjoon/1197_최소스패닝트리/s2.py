import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

import heapq

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

distance = [0 for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]
linked_node = [0 for _ in range(V + 1)]

q = [(0, 1, 0)]

while q:
    cost, now, prev = heapq.heappop(q)
    if visited[now]:
        continue

    visited[now] = True
    distance[now] = cost
    linked_node[now] = prev

    for val, node in graph[now]:
        heapq.heappush(q, (val, node, now))

print('최소 스패팅 트리 가중치 합: ', sum(distance))
print('연결된 노드: ', linked_node)