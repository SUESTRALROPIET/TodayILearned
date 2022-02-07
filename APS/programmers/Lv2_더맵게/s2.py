import heapq

def solution(scoville, K):
    answer = 0
    
    def heapsort(input_lst):        # 힙 정렬: 모든 값을 힙으로 푸시한 다음 한 번에 하나씩 가장 작은 값을 팝하여 구현할 수 있다
        sorted_lst = []
        for num in input_lst:
            heapq.heappush(sorted_lst, num)
        return sorted_lst

    scoville = heapsort(scoville)
    while True:
        fst = heapq.heappop(scoville)   # 가장 작은 수 반환

        if fst >= K:        # 가장 작은 수가 K이상이면 반복문 종료
            break

        if not scoville:    # 가장 작은 수가 K미만이고, 합칠 수가 없다면 -1 반환
            answer = -1
            break

        answer += 1         # 계산 횟수 추가

        scd = heapq.heappop(scoville)   # 두번째로 작은 수 
        new_food = fst + (scd * 2)

        heapq.heappush(scoville, new_food)  # 새로운 값 heappush
    
    return answer

