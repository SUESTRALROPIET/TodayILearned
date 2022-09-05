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