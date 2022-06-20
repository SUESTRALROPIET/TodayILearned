## Lv.2 H-Index

https://programmers.co.kr/learn/courses/30/lessons/42747

#### 1. 정답이 가능한 큰 값부터 탐색하기

```python
def solution(citations):
    
    answer = len(citations) # 정답이 가능한 최대값
    
    while True:
        cnt = len(citations) # 논문 개수: 논문 전체 개수
        
        for ele in citations:   # 원소들 모두 탐색
            if ele < answer:       # 논문이 answer 미만으로 인용됐다면
                cnt -= 1             # cnt - 1
            if cnt < answer:     # 논문개수(cnt)가 answer번 미만이면
                break                   # 다음 논문 탐색 중지
        
        if answer <= cnt:    # 논문이 answer번 이상 이면 => 정답!
            break
        
        answer -= 1             # 아니면 => 가능한 answer 최대값 - 1
                
    return answer
```



