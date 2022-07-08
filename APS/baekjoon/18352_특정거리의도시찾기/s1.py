import sys
sys.stdin = open('input.txt')

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

