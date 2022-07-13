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