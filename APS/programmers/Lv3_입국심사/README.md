## Lv.3 입국심사

https://school.programmers.co.kr/learn/courses/30/lessons/43238

#### 1. 이진탐색
> 시간복잡도: O(log N)
> - N의 범위: min_time과 max_time

> SWEA에서 풀어본 문제인데 또 못 풀었다 ㅠㅠ 

```python
def solution(n, times):
    times.sort()

    min_time = times[0]         # 최소한 걸리는 시간
    max_time = times[-1] * n    # 최대한 걸리는 시간

    while min_time <= max_time:     # min_time과 max_time 범위 좁혀가면서 체크
        mid_time = (min_time + max_time) // 2   # 중간걊
        # print(mid_time, '//', min_time, max_time, '=>', person)
        
        person = 0                      # 통과 가능한 사람 수 초기화
        for desk in times:          # 검사대 리스트 반복하면서 통과간으한 사람 수 연산
            person += mid_time // desk
        
        if person < n:                  # 목표값에 비해 사람 수 부족하면 => mid_time
            min_time = mid_time + 1     # 최소값 증가시켜서 범위 좁히기

        else:
            time = mid_time             # 일단 시간을 저장하고
            max_time = mid_time - 1     # max_time의 범위를 좁힌다.
    
    return time
```