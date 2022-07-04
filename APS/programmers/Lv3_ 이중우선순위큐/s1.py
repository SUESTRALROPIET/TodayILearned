import heapq

def solution(operations):    
    max_heap = []   # 최대힙
    min_heap = []   # 최소힙
    
    for op in operations:
        code, num = op.split()
        num = int(num)
        if code == 'I':     # 원소 추가
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)

        elif max_heap and min_heap:
            if num == 1:    # 최대값 반환
                heapq.heappop(max_heap)
                min_heap.pop()
            else:           # 최소값 반환
                heapq.heappop(min_heap)
                max_heap.pop()
    
    if max_heap and min_heap:
        max_num = heapq.heappop(max_heap)
        min_num = heapq.heappop(min_heap)
        return [-max_num, min_num]
    else:
        return [0, 0]
