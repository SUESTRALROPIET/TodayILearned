## Lv.4 징검다리
> 꼭!!! 다시 풀어봐야할 문제

https://school.programmers.co.kr/learn/courses/30/lessons/43236

#### 1. 이진탐색 참고했는데 또 틀... 
> 틀린 풀이

#### 2. 이진탐색
> [참고 풀이](https://deok2kim.tistory.com/122)
>
> - answer의 최소값은 1, 최대값은 주어진 distance라는 것을 활용하여 이진탐색

> 시간복잡도: O(log N)

```python
  def solution(distance, rocks, n):
      answer = 0
      
      rocks.sort()
      rocks.append(distance)
      
      min_dist = 0
      max_dist = distance
      
      
      while min_dist <= max_dist:
          now = 0
          mid = (min_dist + max_dist) // 2
          cnt = 0
          
          for rock in rocks:
              diff = rock - now
              if diff >= mid:     # 거리 mid가 최소값이 되어야하니까
                  now = rock      # mid보다 큰 돌은 save, 작은 돌은 제거
              else:
                  cnt += 1

          if cnt <= n:
              answer = mid        # [#추가 후, 해결!] answer값을 mid로 갱신
              min_dist = mid + 1
          else:
              max_dist = mid - 1
              
      return answer
```
