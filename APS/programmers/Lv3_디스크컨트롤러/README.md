## Lv.2 디스크 컨트롤러

https://programmers.co.kr/learn/courses/30/lessons/42627

#### 1. deque & heapq 활용하기
> 풀이 과정
> 1. 시작 가능한 순서대로 업무 정렬 후 deque의 popleft로 업무 waitings 배열에 추가
> 2. waitings 배열에서 업무 꺼낼 때, 걸리는 시간이 적은 것부터 꺼내기 위해 heapq(최소힙) 활용
> 
> 시간복잡도: O(log N) 의 2배의 시간이 걸릴 것으로 예상
> - popleft로 업무를 반환하는 것은 시간복잡도가 O(1)이나, heapq를 활용하여 원소 추가/삭제가 무조건 각각 한 번씩 일어나기 때문

```python
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
```
