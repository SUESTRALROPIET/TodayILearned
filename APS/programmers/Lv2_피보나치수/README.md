## Lv.2 피보나치 수

https://school.programmers.co.kr/learn/courses/30/lessons/12945

#### 1. 반복문으로 미리 계산해서 저장 후 꺼내쓰기
> 시간복잡도: O(N)

```python
    MAX_NUM = 100001
    fibo = [0 for _ in range(MAX_NUM)]
    fibo[0] = 0
    fibo[1] = 1
    for i in range(2, MAX_NUM):
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 1234567
        
    def solution(n):
        return fibo[n]
```
