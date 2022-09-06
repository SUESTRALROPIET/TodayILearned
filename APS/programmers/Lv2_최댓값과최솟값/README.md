## Lv.2 최댓값과 최솟값

https://school.programmers.co.kr/learn/courses/30/lessons/12939

#### 1. 
> 시간복잡도: O(N)

```python
    def solution(s):    
        max_num = float('-inf')
        min_num = float('inf')
        
        s = s.split(" ")

        for num in s:
            num = int(num)
            if max_num < num:
                max_num = num
            if num < min_num:
                min_num = num
                
        answer = [min_num, max_num]
        answer = ' '.join(map(str, answer))
            
        return answer
```