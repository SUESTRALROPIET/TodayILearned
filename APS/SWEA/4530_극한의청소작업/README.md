## 4530_극한의 청소 작업

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWO6cgzKOIEDFAWw
#### 1. 4를 제외해야하므로 4가 없는 9진수 > 10진수 변환하여 풀기

> - 아이디어를 생각해내지 못해서 다른 사람 풀이를 참고해서 풀었다.
> - 4를 제외해야하므로 4가 없는 9진수로 변환한다는 것을 생각해내기 어려웠다.


```python
def get_difference(input_str):  # 0 ~ 현재 위치의 차이값을 구할 함수
    return_int = 0      # 10진수 > 9진수 > 10진수 과정을 거친 값을 담아줄 변수 초기화
    
    N = len(input_str)      # input_str 길이
    for idx in range(N):    # idx: 0 > N-1
        ele_int = int(input_str[idx])   # input_str 각 자리 int로 변환
        if 4 < ele_int:     # 자리수가 4보다 크면 -1 해서 4가 없는 9진수 만들기
            ele_int -= 1    
        return_int += ele_int * (9 ** (N-idx-1))    # 9진수 > 10진수로 변환

    return return_int   

T = int(input())
for test in range(1, T+1):
    start, end = map(int, input().split())

    is_minus = False    # start & end 사이에 0이 존재하는 경우 기록하기
    if start < 0 and 0 < end:   
        is_minus = True
        
    # 입력값 > 절대값 > str 변환해서 함수 호출
    start = get_difference(str(abs(start)))     
    end = get_difference(str(abs(end)))

    if is_minus:    # start & end 사이에 0이 존재하는 경우: 0 빼주기
        result = start + end
        result -= 1
    else:                           # Test Case 2개 틀림
        result = abs(start - end)   # start와 end 모두 - 층일 경우가 있을 수 있기 때문에: 절대값 처리 ! 

    print('#{} {}'.format(test, result))
```

#### 2. DP로 풀기

> 구현하지 못함

 ```python
 ```

