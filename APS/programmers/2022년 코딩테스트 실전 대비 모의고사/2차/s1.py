def solution(number):
    def dfs(cnt, idx_list, now):
        nonlocal answer

        idx_list.sort()
        if cnt == 3:
            if sum(now) == 0 and idx_list not in answer:
                answer.append(idx_list)
            return

        for idx in range(N):
            if visited[idx]:
                continue

            visited[idx] = True
            dfs(cnt+1, idx_list + [idx], now + [number[idx]])
            visited[idx] = False

    answer = []
    N = len(number)
    visited = [False for _ in range(N)]
    dfs(0, [], [])

    return len(answer)