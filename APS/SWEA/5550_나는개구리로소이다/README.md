## 5550_나는 개구리로소이다

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWWxqfhKAWgDFAW4&categoryId=AWWxqfhKAWgDFAW4&categoryType=CODE&problemTitle=5550&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

#### 1. 각 문자열의 idx를 활용하여, 리스트 원소를 pop하여 구하기
> 제한시간 초과

 ```python
 T = int(input())
 for test in range(1, T+1):
 
     input_str = list(input())
     frog = ['c', 'r', 'o', 'a', 'k']
 
     input_idx = 0
     frog_idx = 0
 
     cnt = 1
 
     while input_str:    # input 문자열 반복하면서
         if frog_idx == 5:   # frog_idx가 끝까지 가면 다시 0으로 초기화
             frog_idx = 0
 
         if len(input_str) <= input_idx: # input문자열 끝까지 검사했으면
             if frog_idx == 0:       # frog idx가 초기화된 상태(frog idx 반복이 끝났다는 것을 의미)이면,
                 input_idx = 0           # input idx 초기화해서 다시 처음부터 검사하고
                 cnt += 1                # 개구리 수 추가
             else:
                 cnt = -1            # 모두 해당되지 않으면 불가능한 울음소리 이므로 -1 반환후 반복문 종료
                 break
 
 
         input_ele = input_str[input_idx]
         frog_ele = frog[frog_idx]
 
         if input_ele == frog_ele:   # input/frog 문자열이 동일하면 input 문자열 pop해서 제거 후
             input_str.pop(input_idx)
             frog_idx += 1           # 다음 frog 문자 탐색
         else:
             input_idx += 1          # 아니면 다음 input문자열 탐색
 
     if frog_idx != 5:   # 모두 반복이 끝났는데 frog_idx가 5가 아니면 => 불가능한 울음소리이므로 -1 반환
         cnt = -1
 
     print('#{} {}'.format(test, cnt))
 ```



### 2. 다음 원소를 기록하기 전에 앞 원소의 개수와 비교하며 기록하기

> 'croak' 모두 서로 다른 문자로 이루어져 있으며, 앞 문자가 오기 전에 뒤 문자가 나올 수 없기 때문에

```python
T = int(input())
for test in range(1, T+1):

    input_str = list(input())
    frog = ['c', 'r', 'o', 'a', 'k']    # 개구리 울음소리에 해당하는 문자열 리스트
    cnt_lst = [0, 0, 0, 0, 0]           # frog 원소 개수 기록하기

    result = 0      # 개구리 수 세기

    for ele in input_str:   # 주어진 input 문자열 끝까지 반복
        for frog_idx in range(5):   # 개구리 울음소리 길이만큼 반복: 0 -> 4
            if ele == frog[frog_idx]:   # input 문자열 원소가 frog 원소와 같다면
                if frog_idx == 0:           # 해당 원소의 idx가 0이면! 시작을 의미
                    if cnt_lst[4]:              # 울음을 다 끝낸 개구리가 있다면
                        for idx in range(5):        # cnt_lst의 모든 원소를 -1을 해준다.
                            cnt_lst[idx] -= 1
                        result = cnt_lst[0]         # 개구리 수 갱신: 결국 cnt_lst 첫번째값이 개구리 수가 됨.
                    cnt_lst[0] += 1             # ele의 idx값과 대응하는 cnt_lst 원소에 1 추가
                    result = cnt_lst[0]         # 개구리 수 갱신
                    break
                elif cnt_lst[frog_idx] < cnt_lst[frog_idx-1]:   # idx 1 ~ N-1: 앞 원소보다 현재 idx값이 작으면 가능한 울음소리 이므로
                    cnt_lst[frog_idx] += 1                          # ele의 idx값과 대응하는 cnt_lst 원소에 1 추가
                    break
                else:
                    result = -1     # 앞 원소보다 현재 idx값이 크면 => 불가능한 울음소리
                    break

        if result == -1:    # 위 반복문에서 나갈 수 있도록 추가
            break

    if cnt_lst[-1] != cnt_lst[0]:   # 첫번째 cnt값과 마지막 cnt값이 같지 않다면 => 불가능한 울음소리
        result = -1

    print('#{} {}'.format(test, result))
```

