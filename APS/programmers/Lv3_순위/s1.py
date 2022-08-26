def solution(n, results):
    def get_cnt(node, lst):     # node에서 출발했을 때, 갈 수 있는 노드 개수 반환
        visited = [0 for _ in range(n+1)]
        stack = [node]
        while stack:
            now = stack.pop()
            visited[now] = 1
            for next_node in lst[now]:
                if visited[next_node]:
                    continue
                visited[next_node] = 1
                stack.append(next_node)
        return sum(visited)

    answer = 0
    
    win_lst = [[] for _ in range(n+1)]
    lose_lst = [[] for _ in range(n+1)]
    
    for result in results:
        win, lose = result
        win_lst[lose].append(win)
        lose_lst[win].append(lose)
    
    for start in range(1, n+1):
        win_cnt = get_cnt(start, win_lst)
        lose_cnt = get_cnt(start, lose_lst)

        if win_cnt + lose_cnt == n+1:
            answer += 1
            
    return answer