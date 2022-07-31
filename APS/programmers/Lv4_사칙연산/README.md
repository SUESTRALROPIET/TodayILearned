## Lv.4 사칙연산

https://school.programmers.co.kr/learn/courses/30/lessons/1843

#### 1. DFS
> 효율성테스트 통과 X

> 시간복잡도: O(N^2)
> - 현재 배열에 있는 연산자를 하나씩 줄여나가며 길이가 3이 될때까지 연산함

#### 2. DP: '-' 이후 최솟값/최댓값 기록하면서 풀기
> 참고: [참고 풀이](https://tiktaek.tistory.com/33)

> 시간복잡도: O(N)

```python
  def solution(arr):
      min_val = 0
      max_val = 0
      
      N = len(arr)
      now_sum = 0
      
      for idx in range(N-1, -1, -1):
          if arr[idx] == '+':
              continue

          elif arr[idx] == '-':
              nxt_ele = int(arr[idx+1])
              
              a = -now_sum + min_val      # 최솟값 경우 1
              b = -(now_sum + max_val)    # 최솟값 경우 2
              c = -(now_sum + min_val)                # 최댓값 경우 1
              d = now_sum - (2 * nxt_ele) + max_val   # 최댓값 경우 2

              min_val = min(a, b)
              max_val = max(c, d)
              
              now_sum = 0     # 누적값 초기화

          else:
              now_sum += int(arr[idx])
      
      return max_val + now_sum
```
