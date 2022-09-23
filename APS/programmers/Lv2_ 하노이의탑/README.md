## Lv.2 하노이의 탑

https://school.programmers.co.kr/learn/courses/30/lessons/12946

#### 1. 
> [풀이 참고](https://velog.io/@kwb020312/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%95%98%EB%85%B8%EC%9D%B4%EC%9D%98-%ED%83%91)

> 시간복잡도: O(2^n + 2^(n-1) + ... + 1)

```python
  def solution(n):
      answer = []

      def hanoi(depth, fr, to, mid):
          if depth == 1:
              answer.append([fr, to])
              return
          hanoi(depth-1, fr, mid, to)
          answer.append([fr, to])
          hanoi(depth-1, mid, to, fr)

      hanoi(n, 1, 3, 2)
      return answer
```