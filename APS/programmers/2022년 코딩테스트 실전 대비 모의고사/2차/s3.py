import heapq

def solution(n, roads, sources, destination):
    answer = []

    linked_lst = [[] for _ in range(n+1)]
    for road in roads:
        fr, to = road
        linked_lst[fr].append(to)
        linked_lst[to].append(fr)

    for source in sources:
        find_dest = False
        q = [(0, source)]
        checked = [False for _ in range(n+1)]

        while q:
            cnt, now = heapq.heappop(q)
            if now == destination: 
                find_dest = True
                answer.append(cnt)
                break
            if checked[now]:
                continue
            checked[now] = True
            for ele in linked_lst[now]:
                if not checked[ele]:
                    heapq.heappush(q, (cnt+1, ele))
                
        if not find_dest:
            answer.append(-1)

    return answer