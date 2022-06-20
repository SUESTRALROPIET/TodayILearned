import sys
sys.stdin = open('input.txt')

import heapq

def break_edges(node):
    if node == S:
        return
    his_node = history[node]
    edges[his_node][node] = 0
    break_edges(his_node)

def dijkstra(start_node):
    q = []
    heapq.heappush(q, (0, start_node))

    while q:
        distance, node = heapq.heappop(q)

        if cnt[node] < distance:
            continue
        for target_node in range(N):
            plus_distance = edges[node][target_node]
            if not plus_distance:
                continue
            new_distance = distance + plus_distance
            if new_distance < cnt[target_node]:
                cnt[target_node] = new_distance
                history[target_node] = node
                heapq.heappush(q, (new_distance, target_node))                  

while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break
    
    edges = [[0] * N for _ in range(N)]
    history = [0] * N

    S, D = map(int, input().split())

    for _ in range(M):
        U, V, P = map(int, input().split())
        edges[U][V] = P

    cnt = [float('INF')] * N
    dijkstra(S)
    answer = cnt[D]

    while answer == cnt[D]:
        break_edges(D)

        cnt = [float('INF')] * N
        dijkstra(S)

    if cnt[D] == float('INF'):
        print(-1)
    else:
        print(cnt[D])
