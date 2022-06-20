## Lv.2  주식가격

https://programmers.co.kr/learn/courses/30/lessons/42584

#### 1. 이중 for문으로 값 비교
```python
def solution(prices):

    N = len(prices)
    answer = [0] * N    # prices 길이만큼 배열 생성
    
    for i in range(N):          # i: 0 > N-1
        for j in range(i+1, N): # j: i > N-1
            answer[i] += 1              # 1초 추가
            if prices[i] > prices[j]:   # 값이 더 적으면 break
                break

    return answer
```