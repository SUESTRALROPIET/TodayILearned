# 사전학습

#### 1. nonlocal문

https://docs.python.org/ko/3/reference/simple_stmts.html?highlight=global#grammar-token-python-grammar-nonlocal_stmt

```python
nonlocal_stmt ::=  "nonlocal" identifier ("," identifier)*
```


nonlocal 문은 나열된 식별자들이 **전역을 제외하고 가장 가까이서 둘러싸는 스코프에서 이미 연결된 변수를 가리키도록 만듭니다**. 이것은 중요한데, 연결의 기본 동작이 지역 이름 공간을 먼저 검색하는 것이기 때문입니다. 이 문장은 캡슐화된 코드가 전역 (모듈) 스코프 외에 지역 스코프 밖의 변수들에 재연결할 수 있도록 합니다.

nonlocal 문에 나열된 이름들은, global 문에 나열된 것들과는 달리, 둘러싼 스코프에서 이미 존재하는 연결들을 가리켜야만 합니다 (새 연결이 어떤 스코프에 만들어져야만 하는지 명확하게 결정할 수 없습니다).

nonlocal 문에 나열되는 이름들은 지역 스코프에 이미 존재하는 연결들과 겹치지 않아야 합니다.



## Lv.2 타겟넘버

https://programmers.co.kr/learn/courses/30/lessons/43165

#### 1. dfs 활용하기

```python
def solution(numbers, target):    
    answer = 0                      # 타겟 넘버가 되는 횟수 
    max_level = len(numbers)        # dfs 깊이: 리스트 길이
    
    def dfs(now_value, now_level):  # dfs(현재 값, 현재 level/깊이)
        
        if now_level == max_level:      # 모든 리스트 원소를 탐색했다면
            if now_value == target:         # target 값인지 확인 후 
                nonlocal answer                 # nonlocal: 가장 가까이서 둘러싸는 스코프에서 이미 연결된 변수를 가리킨다.
                answer += 1                     # answer에 횟수 1 더하기
            return
        
        for i in range(2):          # (0: 원소 빼기, 1: 원소 더하기)
            if i:
                dfs(now_value + numbers[now_level], now_level+1)
            else:
                dfs(now_value - numbers[now_level], now_level+1)
    
    dfs(0, 0)
        
    return answer
```

