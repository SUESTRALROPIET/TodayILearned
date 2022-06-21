## Lv.2 이진 변환 반복하기

https://programmers.co.kr/learn/courses/30/lessons/70129

#### 1. 단순 반복으로 순회 + 재귀로 풀기
> 시간복잡도: O(n)
> - 정확한 시간복잡도는 잘 모르겠지만, 초기 입력값의 최대 길이가 150,000이고, '0'이 하나 밖에 없어도 n(입력값의 길이)의 제곱만큼 걸리진 않는다.
> - O(n)보다는 크지만 O(n^2)만큼 걸리진 않을 것으로 예상된다.

```python
    # 이진수(문자열)로 변환하는 함수
    def get_binary(input_int):
        return_str = ''
        while input_int:
            if input_int % 2 == 0:
                return_str = '0' + return_str
            else:
                return_str = '1' + return_str
            input_int //= 2
        return return_str

    def solution(s):
        def one_step(input_str):
            nonlocal answer_step, answer_zero
            
            answer_step += 1
            
            N = len(input_str)
            zero_cnt = 0
            
            for ele in input_str:   # '0' 개수 세기
                if ele == '0':
                    zero_cnt += 1
            
            answer_zero += zero_cnt # '0' 개수 취합

            N -= zero_cnt
            
            if N == 1:  # 1이면 재귀 종료
                return
            else:       # 아니면, 2진수 변환 후 재귀
                new_str = get_binary(N)
                return one_step(new_str)
                
        answer_step = 0
        answer_zero = 0
        
        one_step(s)
            
        return [answer_step, answer_zero]
```




