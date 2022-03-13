## Lv.2 소수 찾기

https://programmers.co.kr/learn/courses/30/lessons/42839

## 소수 판별법
> 참고 사이트: https://makedotworld.tistory.com/13

**n이 소수인지 아닌지 판별하기 위해서는 루트 n 이하의 수만 나눠보면 된다**
- 루트 n 이하까지 탐색하는 이유
  1. 합성수 X = N * M (N <= M)
  2. N * M <= M * M
  3. X <= M ** 2
  4. X ** 0.5 <= M


#### 1. 조합이 가능한 수 dfs로 탐색 + 소수 판별하기

```python
def solution(numbers):
                
    answer = 0      # 소수 개수
    answer_lst = [] # 조합이 가능한 숫자 리스트

    # 소수(Prime Number) 인지 체크하기 
    def check(num):
        nonlocal answer
        if num == 0 or num == 1:    # 0 또는 1 => 소수X
            return
        i = 2                       # 2부터 탐색
        k = int(num ** 0.5)
        while i <= k:           # i: i -> 루트 num 값
            if num % i == 0:        # 나머지 없이 나눠지면 => 소수 X
                return
            else:                   # 나머지 있으면 => 다음 i로 재탐색
                i += 1

        answer += 1                 # i부터 루트num값까지 탐색 완료 => 소수 O

    # target_level 길이 숫자조합하기 
    def get_num(now, level, target_level):
        if level == target_level:   # target_level만큼 숫자 길이가 차면
            now = int(now)
            if not now in answer_lst:   # answer_lst에 없을 경우에만 추가
                answer_lst.append(int(now))
            return 
        
        for idx in range(max_len):
            if checked[idx]:
                continue
            checked[idx] = 1
            get_num(now+numbers[idx], level+1, target_level)
            checked[idx] = 0
        
    numbers = list(numbers) # 입력값 자료형 리스트로 변경
    max_len = len(numbers)  # 숫자 전체 길이
    checked = [0] * max_len # 사용한지 체크
    
    for num_len in range(1, max_len+1): # 숫자 길이:  1 ~ 숫자 전체길이
        get_num('', 0, num_len)             # 숫자 길이만큼 조합하기
        
    for ele in answer_lst:  # 소수인지 검사하기
        check(ele)

    return answer
```

