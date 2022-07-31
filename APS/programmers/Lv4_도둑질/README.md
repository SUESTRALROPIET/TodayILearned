## Lv.4 도둑질

https://school.programmers.co.kr/learn/courses/30/lessons/42897

#### 1. DP테이블에 값 기록하기
> [참고 풀이](https://school.programmers.co.kr/questions/31576)

> 시간복잡도: O(N)

```python
    def solution(money):    
        N = len(money)
        fst = [0] + money[:-1]
        scd = [0] + money[1:]
        
        for idx in range(2, N):      
            fst[idx] = max(fst[idx]+fst[idx-2], fst[idx-1])
            scd[idx] = max(scd[idx]+scd[idx-2], scd[idx-1])
            
        return max(fst[-1], scd[-1])
```
