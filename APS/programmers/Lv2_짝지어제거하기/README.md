## Lv.2 짝지어제거하기

https://programmers.co.kr/learn/courses/30/lessons/12973

#### ~~1. 문자열을 리스트로 변환 후, idx를 활용하기~~

> - 3-9 문제 시간초과 / 효율성 시간초과

#### ~~2. 문자열을 리스트로 변환 후, 리스트 원소 pop해서 풀기~~

> - 3-9 문제 시간초과 / 효율성 시간초과

#### ~~3. 문자열을 리스트로 변환 후, 리스트 원소 pop & append 해서 풀기~~

> - 2-8 문제 시간초과 / 효율성 시간초과

#### 4. 같은 문자인지 검사 후 pop하기

```python
def solution(s):
    stack = []

    for ele in s:                           # input값 s 끝까지 탐색
        if len(stack) and stack[-1] == ele:     # stack에 쌓인 원소가 있고 /and/ input원소가 stack 가장 위에 있는 원소와 같다면
            stack.pop()                             # stack에서 제거
        else:
            stack.append(ele)                       # stack에 추가

    if stack:       # stack에 남아 있는 원소가 있으면 => 0 반환
        return 0
    else:           # 없으면 => 1 반환
        return 1
```
