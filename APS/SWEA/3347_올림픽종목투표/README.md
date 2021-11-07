## 3347_올림픽 종목 투표

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWDTHsZ6r0EDFAWD&categoryId=AWDTHsZ6r0EDFAWD&categoryType=CODE&problemTitle=%EC%98%AC%EB%A6%BC%ED%94%BD&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

#### 1. 이중 for문을 사용해서 score_list의 최대값 인덱스 반환

```python
T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    sport_list = list(map(int, input().split()))
    person_list = list(map(int, input().split()))

    score_list = [0] * N
    result_idx = 0
    max_score = 0

    for person in person_list:
        for idx in range(N):
            if sport_list[idx] <= person:
                score_list[idx] += 1
                if max_score < score_list[idx]:
                    result_idx = idx
                    max_score = score_list[idx]
                break
    
    print('#{} {}'.format(test, result_idx+1))
```



