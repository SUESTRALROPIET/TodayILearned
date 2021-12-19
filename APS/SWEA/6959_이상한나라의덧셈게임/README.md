## 6959_이상한 나라의 덧셈게임

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWjlH0k63joDFAVT

#### ~~1. DFS로 한 자리 숫자가 될때까지 연산하기~~

> 시간 초과

```py
def next_level(now_str, times):
    global result

    N = len(now_str)

    if N == 1:
        result = times
        return
        
    for start_idx in range(N-1):
        new_num = int(now_str[start_idx]) + int(now_str[start_idx+1])
        new_str = now_str[:start_idx] + str(new_num) + now_str[start_idx+2:]
        
        next_level(new_str, times+1)


T = int(input())
for test in range(1, T+1):
    num_lst = input()

    result = 0

    next_level(num_lst, 1)

    if result % 2:
        winner = 'B'
    else:
        winner = 'A'
    
    print('#{} {}'.format(test, winner))
```



#### 2. 두수를 계산하면서 탐색하기

> 자릿수마다 모든 경우를 탐색할 필요가 없었다.
>
> - 최선의 방법은 없다: 연속된 두 수가 어떤 수인지 상관없이 승/패의 결과는 같다

 ```python
 T = int(input())
 for test in range(1, T+1):
     str_num = input()   # 입력값
     cnt = 0             # 횟수 
 
     while 1 < len(str_num):     # str_num 길이가 2 이상일때만 실행
         new_num = str(int(str_num[0]) + int(str_num[1]))    # 첫번째/두번째 숫자 합해서
         str_num = new_num + str_num[2:]                     # 기존 문자열 앞에 붙이기
         cnt += 1                                            # 횟수 추가
     
     if cnt % 2:     # cnt가 홀수이면 => A / 아니면 => B가 승리!
         winner = 'A'
     else:
         winner = 'B'
 
     print('#{} {}'.format(test, winner))
         
 ```

