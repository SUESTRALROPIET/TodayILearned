## Lv.2 JadenCase 문자열 만들기

https://school.programmers.co.kr/learn/courses/30/lessons/12951

#### 1. 반복문 & 조건문
> 시간복잡도: O(N)
>   - N: 문자열 길이

```python
    def solution(s):
        answer = ''
        fst_ele = True
        
        for ele in s:
            if ele == ' ':
                fst_ele = True
                answer += ele
                continue
                
            if fst_ele:
                answer += ele.upper()
                fst_ele = False
            else:
                answer += ele.lower()
        
        return answer
```
