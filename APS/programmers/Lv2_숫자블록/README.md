## Lv.2 숫자블록

https://school.programmers.co.kr/learn/courses/30/lessons/12923

#### 1. 단순하게 약수의 최대값 구하기
> 효율성 테스트: 시간초과

> 문제점
> - n의 제곱근까지 검사해도 되는 조건 X
> - 블럭 최대값 검사 X

#### 2. N의 제곱근까지 검사해서 약수의 최대값 구하기
> 효율성 테스트: 실패

> 문제점
> - 블럭 최대값 검사 X

#### 3. N의 약수 중 최대값 구하기
> [효율성 테스트 힌트](https://school.programmers.co.kr/questions/33585)

> 시간복잡도: O(N)

 ```python
    def get_num(num):   # 약수 중 최대값 구하기
        if num < 2:
            return 0
        m = int(num ** 0.5)
        for std in range(2, m+1):
            ans = num // std
            if num % std == 0:      ### 효율성 테스트 해결 포인트: 
                if ans < 10000000:  ### 몫이 블러 최대값 10000000을 넘을 수 없다.
                    return num // std
        return 1

    def solution(begin, end):
        answer = []
        
        for i in range(begin, end+1):
            answer.append(get_num(i))
        
        return answer
 ```