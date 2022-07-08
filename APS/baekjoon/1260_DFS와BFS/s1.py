import sys
sys.stdin = open('input.txt')

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
