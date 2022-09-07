## Lv.2 최솟값 만들기

https://school.programmers.co.kr/learn/courses/30/lessons/12941

#### 1. 정렬 & 반복문
> 시간복잡도: O(N)

```python
    def solution(A,B):
        answer = 0
        
        N = len(A)

        A.sort()
        B.sort()
        
        for idx in range(N):
            answer += (A[idx] * B[N-1-idx])
        
        return answer
```

#### 2. zip 함수 적용