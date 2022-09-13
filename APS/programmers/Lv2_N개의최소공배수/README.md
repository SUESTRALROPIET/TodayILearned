## Lv.2 N개의 최소공배수

https://school.programmers.co.kr/learn/courses/30/lessons/12953

#### 1. 반복문 + 다중집합(w. deepcopy)
> 시간복잡도: O(N)
>   - num 숫자가 크면 시간복잡도가 커질 가능성이 있다.

```python
    from copy import deepcopy

    def solution(arr):    
        answer = 1
        answer_lst = []
        
        for num in arr:
            ele_lst = []    # num의 약수가 담김
            ele = 2
            while ele <= num + 1:
                if num % ele == 0:
                    ele_lst.append(ele)
                    num //= ele
                else:
                    ele += 1
            
            # 다중집합 연산: 합집합 - 교집합
            temp_ele_lst = deepcopy(ele_lst)
            for ans in answer_lst:
                if ans in temp_ele_lst:
                    temp_ele_lst.remove(ans)
                    
            answer_lst += temp_ele_lst
            
        for ans_ele in answer_lst:
            answer *= ans_ele        
        
        return answer
```
#### 2. gcd 함수 활요 (풀이 참고)
> - GCD, LCM 공식 활용

```python 
    '''
    * 최대공약수(GCD) 함수
    : 최대공약수를 중 가장 큰 수를 반환주는 함수
    : Return the greatest common divisor of the specified integer arguments.
    (예) gcd(10, 100) = 10

    * 최소공배수(LCM) = 두 자연수의 곱 / 최대공약수
    '''
    from math import gcd

    def solution(arr):      
        answer = arr[0]
        for n in arr:
            answer = n * answer // gcd(n, answer)

        return answer
```