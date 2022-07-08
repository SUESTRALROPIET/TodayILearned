import sys
sys.stdin = open('input.txt')

from collections import deque

def DFS(num):
    visited[num] = 1
    print(num, end = " ")
    for next in sorted(edges[num]):
        if not visited[next]:
            DFS(next)

def BFS():
    q = deque([V])
    visited[V] = 1
    while q:
        now = q.popleft()
        print(now, end = " ")
        for next in sorted(edges[now]):
            if not visited[next]:
                q.append(next)
                visited[next] = 1

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
BFS()
