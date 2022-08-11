## Lv.2 땅따먹기

https://school.programmers.co.kr/learn/courses/30/lessons/12913

#### 1. DFS
> 런타임 에러: DFS로 풀면 안되는 문제

### 2. heapq
> 무조건 각 행의 최대값이 결과가 될 수 없음

### 3. dp
> [풀이 참고](https://school.programmers.co.kr/learn/courses/18/lessons/846)

> 시간복잡도: O(N * 4) => O(N)

> - 행렬[i][j]가 가질 수 있는 최대값은 행렬[i][j] + j와 동일한 열을 제외한 행렬[i+1]의 최대값임을 활용

```python
  def solution(land):
      N = len(land)

      for row in range(N-1, 0, -1):
          answer = land[row-1]        # 아래 최대값 구하는 행의 앞 행
          
          for col in range(4):
              answer[col] += max(land[row][:col] + land[row][col+1:])     
      return max(answer)
```
