import heapq
from collections import deque

def solution(jobs):
    answer = 0
    now = 0     # 현재 시간
    
    N = len(jobs)
    jobs.sort()     # 시간 순으로 정렬
    jobs = deque(jobs)  # deque로 => 첫번째 원소 반환하기 위해
    
    waitings = []   # 대기하고 있는 업무 배열
    
    while jobs or waitings:
        # 현재 시간에 가능한 업무 모두 pop한 후, waitings 배열에 추가
        while jobs:
            if jobs[0][0] <= now:
                start_time, value = deque.popleft(jobs)
                heapq.heappush(waitings, (value, start_time))
            else:
                break
                
        if waitings:    # 대기하고 있는 업무 배열이 있을 경우, 업무 수행
            value, start_time = heapq.heappop(waitings)
            now += value
            answer += (now - start_time)
        else:           # 대기하고 있는 업무 배열이 없으면 현재시간 + 1
            now += 1
            
    return answer // N
