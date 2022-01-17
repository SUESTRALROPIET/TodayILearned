## 3752_가능한 시험 점수

https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AWHPkqBqAEsDFAUn&categoryId=AWHPkqBqAEsDFAUn&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=6

#### 1. ~~dfs로 가능한 점수 완전 탐색하기~~

> - 제한시간 초과

```python
def dfs(q_num, score):
    if q_num == N:
        possible_score.add(score)
        return
    dfs(q_num+1, score+score_lst[q_num])       
    dfs(q_num+1, score)       

T = int(input())
for test in range(1, T+1):
    N = int(input())
    score_lst = list(map(int, input().split()))
    possible_score = set()

    dfs(0, 0)
    
    result = len(possible_score)
    print('#{} {}'.format(test, result))

```

#### 2. 최대값만큼 배열 길이 생성 > 나올 수 있는 점수에 체크하기

```python
T = int(input())
for test in range(1, T+1):
    N = int(input())
    score_lst = list(map(int, input().split()))

    max_sum = sum(score_lst)            # 모든 문제를 맞혔을 때 값
    check_score = [0] * (max_sum + 1)   # 나올 수 있는 점수를 체크할 리스트 초기화
    check_score[0] = 1                  # 모두 틀렸을 때 => 0점이 나오므로 체크 

    for score in score_lst:             # 모든 문제 반복
        for check_idx in range(max_sum, -1, -1):    # check_idx: max_sum -> 0   
                                                    ## check_idx: 0 -> max_sum 으로 하면 안됨
            if check_score[check_idx]:              ## 큰 점수부터 반복하면서 점수 더하기 
                check_score[check_idx+score] = 1    ## 나올 수 있는 점수 체크

    result = sum(check_score)   # 체크된 개수 구하기

    print('#{} {}'.format(test, result))
```