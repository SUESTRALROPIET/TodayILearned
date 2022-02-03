## Lv.2 124 나라의 숫자		

https://programmers.co.kr/learn/courses/30/lessons/12899

#### 1. 3으로 나눈 몫 & 나머지 활용하기

```python
def solution(n):
    answer = ''
    num_lst = ['1', '2', '4']

    answer = num_lst[(n%3)-1] + answer  # 한 자리 숫자 변환(1 ~ 3)
                                        # 나머지값을 idx로 표현하기 위해 -1

    while 3 < n:    # 4부터는 while문 반복
        n -= 1          # -1을 해주는 이유: 3의 배수일 때, 다른 값보다 몫이 1이 크다 (예) 4, 5, 6 => 1, 1, 2
        n //= 3
        answer = num_lst[(n%3)-1] + answer    
    return answer
```

