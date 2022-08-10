## Lv.2 다음 큰 숫자

https://school.programmers.co.kr/learn/courses/30/lessons/12911

#### 1. 단순 반복문
> 시간복잡도: O(n...?)
> 최악의 경우여도 시간복잡도가 그렇게 크지 않다.

 ```python
    # 2진수 변환시 '1' 개수 반환
    def get_one(n):
        cnt = 0
        while n:
            cnt += n % 2
            n //= 2
        return cnt

    def solution(n):    
        n_cnt = get_one(n)
        K = n+1
        while True:
            k_cnt = get_one(K)
            if k_cnt == n_cnt:
                return K
            K += 1
 ```