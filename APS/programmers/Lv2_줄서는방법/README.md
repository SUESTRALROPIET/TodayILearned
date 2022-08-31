## Lv.2 줄 서는 방법

https://school.programmers.co.kr/learn/courses/30/lessons/12936

#### 1. DFS 활용한 조합
> 12, 13 테스트케이스: 시간초과
> 효율성테스트: 시간초과

#### 2. 규칙 활용
> 시간복잡도: O(n - 1)

> - 배열 앞 부분부터 채워 넣는다.
> - n이 3이라고 주어졌을 때, 첫번째 자리가 아래와 같다는 것을 활용
>
>   - k가 1 ~ 6이면, 남은 수 중 가장 작은 수
>   - k가 7 ~ 12이면, 남은 수 중 2번째로 작은 수
> - 즉, 뒤에서 n번째 자리는 `(k - 1) // fac_lst[step]` 에 의해 결정된다.
>
>   - `k-1`을 해주는 이유: 나누어 떨어지는 수를 고려해 빼줌
> - step이 1이 될때까지 반본: 뒤에서 2번째 자리까지 계산
> - 남은 수 answer에 더해주면 답 반환

```python
  MAX_N = 20
  fac_lst = [0 for _ in range(MAX_N)]
  fac_lst[1] = 1
  for i in range(2, MAX_N):
      fac_lst[i] = fac_lst[i-1] * i
      
  def solution(n, k):
      num_lst = [i for i in range(1, n+1)]
      answer = []
      
      step = n - 1
      
      while step:
          idx = (k - 1) // fac_lst[step]
          answer.append(num_lst[idx])
          k -= (idx * fac_lst[step])
          del(num_lst[idx])
      
          step -= 1
          
      return answer + num_lst
```