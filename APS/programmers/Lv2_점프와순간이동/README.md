## Lv.2 점프와 순간 이동

https://programmers.co.kr/learn/courses/30/lessons/12980

#### 1. 도착점에서 시작점으로 while문 사용해서 풀기
> 효율성 테스트 2, 3, 4, 9: 시간초과

#### 2. memoization으로 기록해서 동일한 n은 반복 막기
> 시간복잡도: O(log n)
> - n만큼 걸리지는 않고, 그렇다고 n의 값이 항상 ans_dict에 있는 것도 아니기 때문에 O(1)도 아니다.

```python
    ans_dict = {}

    def solution(n):
        ans = 1
        
        while 1 < n:
            if n in list(ans_dict.keys()):  # 기록
                ans += ans_dict[n]
                break

            if n % 2:
                ans += 1
            n //= 2
        
        ans_dict[n] = ans

        return ans
```
#### 3. 1번 풀이에서 불필요한 if문 제거하기
> - 1번 풀이에서 if문을 제거하니 시간초과 문제가 해결됐다.
> - if문으로 검사하나마나한 부분은 추가하지 않는 것이 시간을 줄일 수 있는 방법이다.
```python
    def solution(n):
        ans = 1
        
        while 1 < n:
            ans += n % 2
            n //= 2

        return ans
```

