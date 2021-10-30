## 1233_사칙연산유효성검사

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141176AIwCFAYD&categoryId=AV141176AIwCFAYD&categoryType=CODE&problemTitle=%EC%82%AC%EC%B9%99%EC%97%B0%EC%82%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1



#### 1. dfs로 탐색하기 + 노드에 담긴 값이 숫자이면 1, 연산자이면 0으로 입력받기

1. root_list (노드에 담긴 값)에 입력값을 담을 때, 숫자는 1 / 연산자는 0으로 변환한 후,
2. 자식 노드들을 and 연산하여 루트 노드(노드번호 1번)값을 반환한다.

```python
def dfs(start):
    if not (left_list[start] and right_list[start]):    # 자식 노드가 없으면 root_list 값 반환
        return root_list[start]

    if right_list[start]:                               # 오른쪽 자식 노드가 있으면 (왼쪽 자식 노드도 있으므로) -> 왼쪽 자식 / 오른쪽 자식 and 연산
        return dfs(left_list[start]) and dfs(right_list[start])
    
    else:                                               # 왼쪽 자식만 있으면 왼쪽 자식 값 반환
        return dfs(left_list[start])

for test in range(1, 11):
    N = int(input())
    root_list = [0] * (N+1)
    left_list = [0] * (N+1)
    right_list = [0] * (N+1)

    for _ in range(N):
        a, b, *children = input().split()

        a = int(a)

        if b.isdigit():     # a번 노드 값 b가 숫자이면 -> True
            root_list[a] = True
        else:               # 연산자이면 -> False
            root_list[a] = False

        # left_list, right_list에 자식 노드 번호 담기
        if len(children) == 2:
            left_list[a], right_list[a] = int(children[0]), int(children[1])
        elif len(children) == 1:
            left_list[a] = children
        else:
            continue
    
    if dfs(1):      # 노드번호 1부터 시작하기
        result = 1
    else:
        result = 0

    print('#{} {}'.format(test, result))
```





