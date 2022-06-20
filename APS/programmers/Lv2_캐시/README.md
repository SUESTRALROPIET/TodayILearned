## Lv.2 [1차] 캐시

https://programmers.co.kr/learn/courses/30/lessons/17680

#### 1. deque활용
> 11, 16, 19, 20 틀림
> 
> - queue에 동일한 원소가 있는지 확인하지 않고 캐시 길이만큼 무조건 원소를 추가한 것이 문제가 됨

#### 2. 조건문 수정
>  - deque를 활용한 이유: 가장 오랫동안 참조되지 않은 원소를 제거하기 위해 첫번째 원소 반환하는 자료형으로 적합한 queue를 사용함. 
>       - 일반 리스트에서 첫 번째 원소를 반환하는데 걸리는 시간: O(n)
>       - deque에서 첫 번째 원소를 반환하는데 걸리는 시간: O(1)
> - 시간복잡도: O(n * cacheSize)
>   - n: cities 길이만큼 for문 반복
>   - cacheSize: deque에서 remove할 때 걸리는 시간

```python
from collections import deque

def solution(cacheSize, cities):
    cities = list(map(lambda x: x.upper(), cities))
    answer = 0
    
    q = deque([])

    
    for city in cities:
        if cacheSize == 0:
            answer = len(cities) * 5
            break

        if city in q:
            q.remove(city)
            q.append(city)
            answer += 1
        
        elif len(q) < cacheSize:
            q.append(city)
            answer += 5

        else:
            q.popleft()
            q.append(city)
            answer += 5    

    return answer
```




