## 1222_계산기1

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14mbSaAEwCFAYD&categoryId=AV14mbSaAEwCFAYD&categoryType=CODE&problemTitle=%EA%B3%84%EC%82%B0%EA%B8%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1



#### 1. 입력값을 '+' 기준으로 split하여 => 리스트의 합으로 결과 반환하기

```python
for test in range(1, 11):
    N = int(input())
    input_list = list(map(int, input().split('+')))
    print('#{} {}'.format(test, sum(input_list)))
```

> 후위 표기식으로 바꾸는 부분이 생략됨

​				  

#### 2. 후위 표기식으로 변환 후 연산하기

1. 후위 표기식으로 변환
   - 피연산자이면 출력
   - 연산자이면 담긴 연산자 출력 후 새 연산자 스택에 쌓기
2. 후위 표기식 계산
   - 피연산자이면 스택에 쌓기
   - 연산자이면 연산 후 스택에 담기

```python
for test in range(1, 11):
    N = int(input())
    input_list = list(input())

    # 후위 표기식으로 변환하기
    op_stack = []
    postfix = ''

    while 0 < len(input_list):
        ele = input_list.pop(0)
        if ele.isdigit():
            postfix += ele
        elif op_stack:
            postfix += op_stack.pop()
            op_stack.append(ele)
        else:
            op_stack.append(ele)
    postfix += op_stack.pop()

    num_stack = []
    for ele in postfix:
        if ele.isdigit():
            num_stack.append(ele)
        else:
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(int(a)+int(b))

    print('#{}'.format(test), *num_stack)
```







