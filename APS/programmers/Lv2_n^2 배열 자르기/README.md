## Lv.2 n^2 배열 자르기

https://programmers.co.kr/learn/courses/30/lessons/87390

#### 1. 규칙 찾아 연산하기
> 시간복잡도: O(n)
> - left ~ right+1 까지 순회하는 만큼 걸림

```python
def solution(n, left, right):
    
    def return_num(num):    # idx에 해당하는 수 반환하기
        share, remain = divmod(num, n)
        if remain <= share:
            return share + 1
        else:
            return remain + 1
    
    answer = []
    
    for idx in range(left, right+1):
        answer.append(return_num(idx))
    
    return answer
```
