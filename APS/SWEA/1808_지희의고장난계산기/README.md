## 1808. 지희의 고장난 계산기

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4yC3pqCegDFAUx

#### 1. ~~피연산자 3개 이상인 경우~~ FAIL

#### 2. 가능한 조합으로 DFS하기

> 1. 바로 숫자를 누를 수 있는지 여부 확인
> 2. 바로 누를 수 없다면, 누를 수 있는 숫자로 [1 ~ 목표값 길이] 자리수를 가진 숫자 조합하기
>    - 큰 수가 몫 or 나누는 수가 될 수 있다면 버튼을 누르는 횟수가 적을 가능성이 높으므로, 내림차순 정렬하기
> 3. 조합한 숫자 리스트를 반복하면서, 주어진 target값을 나눠 몫이 누를 수 있는 숫자가 될때까지 반복한다.

```python
import itertools

def get_result(share, cnt):
    global min_result

    for num in num_lst:
        if num == 0 or num == 1:  # num이 0이거나 1이면 연산 X
            continue

        if share < num:           # num이 나눌 수(share)보다 크면 연산 X
            continue

        if share % num == 0:            # 나누어 떨어지면
            new_share = share // num        # new_share에 몫을 저장하고

            if new_share not in num_lst:    # new_share가 바로 조합할 수 없는 숫자이면
                return get_result(new_share, cnt + len(str(num)) + 1)   # 몫으로 다시 탐색하기

            result = cnt + len(str(new_share)) + 1 + len(str(num)) + 1   # 지금까지 횟수 + 몫 길이 + 나누는 수 길이

            if result < min_result:         # result가 min_result보다 작으면 반환
                min_result = result
            return
    return

T = int(input())
for test in range(1, T+1):
    if test == 8:
        pass
    input_num = list(map(int, input().split()))     # (int) 0 ~ 9까지 가능 유무 => 1 / 0으로 이루어진 리스트
    target = input()                                # (str) 목표값
    N = len(target)                                 # 목표값 길이

    ### 누를 수 있는 숫자 possible_num에 담기
    possible_num = []                               # 가능한 숫자 담을 빈 리스트
    for idx in range(10):                           # idx: 0 > 9
        if input_num[idx]:                         
            possible_num.append(idx) 

    possible_num = list(map(str, possible_num))     # int > str 으로 변환하기

    get_comb = False        # get_comb 연산 여부 

    for target_ele in target:
        if target_ele in possible_num:  # target 숫자 모두 바로 누를 수 있으면
            continue
        else:                           # target 숫자 모두 바로 누를 수 없으면
            get_comb = True

    if get_comb:        # 바로 누를 수 없는 숫자는 조합을 조합하러 가기
        num_lst = []    # 가능한 조합을 담을 빈 리스트 초기화
        for i in range(1, N+1):     # 1 ~ N+1 의 자리 숫자 조합
            num_lst += list(map(''.join, itertools.product(possible_num, repeat=i)))

        num_lst = list(set(map(int, num_lst)))      # 문자열인 숫자들을 정수형으로 바꿔 줌 => '01'과 같은 조합을 1로 변경 + set으로 중복 제거
        num_lst.sort(reverse=True)                  # 큰 수 먼저 탐색하기 위해서 내림차순 정렬

        min_result = float('INF')   # 가장 적은 횟수를 담을 변수 초기화

        get_result(int(target), 0)

    else:
        min_result = N + 1  # target 숫자 길이 + 등호 연산자 개수 

    if min_result == float('INF'):  # min_result에 변화가 없으면 => 모든 수가 불가능함을 의미
        min_result = -1

    print('#{} {}'.format(test, min_result))

```



