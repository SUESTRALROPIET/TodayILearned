## Lv.2 숫자의 표현

https://school.programmers.co.kr/learn/courses/30/lessons/12924

#### 1. 연속된 숫자의 합 활용
> 시간복잡도: O(N/2)

 ```python
    def solution(n):
        answer = 1
        '''
        연속된 숫자의 합인 아래 규칙 활용
            1: n
            2: 2n + 1
            3: 3n
            4: 4n + 2
            5: 5n
            6: 6n + 3
            ...
        '''
        for i in range(2, n//2 + 2):
            share, remain = divmod(n, i)

            # 유효성 검사: 17번 테케 해결
            if i % 2 == 0:
                min_num = share - (i // 2 - 1)
            else:
                min_num = share - (i // 2) 
                
            if min_num <= 0:
                continue

            # i가 짝수/홀수 일때 조건
            if i % 2 == 0 and remain != i // 2:
                continue
                
            elif i % 2 and remain:
                continue

            answer += 1
        
        return answer

 ```

#### 2. 단순하게 풀어도 해결 가능!