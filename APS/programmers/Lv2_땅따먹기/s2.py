import heapq

def solution(land):
    answer = 0
    N = len(land)
    prev_idx = -1

    matrix = []
    for ele in land:
        q = []
        for idx, val in enumerate(ele): 
            heapq.heappush(q, (-val, idx))
        matrix.append(q)

        while q:
            val, idx = heapq.heappop(q)
            if idx == prev_idx:
                continue
            answer += val
            prev_idx = idx
            break
        
    return -answer