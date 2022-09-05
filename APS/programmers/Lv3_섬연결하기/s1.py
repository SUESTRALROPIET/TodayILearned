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