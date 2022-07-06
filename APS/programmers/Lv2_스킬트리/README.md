## Lv.2 스킬트리

https://school.programmers.co.kr/learn/courses/30/lessons/49993

#### 1. 반복문 & 델타이동
> 시간 복잡도: O(1)
> - deque를 사용하여 원소를 꺼내는데 걸리는 시간은 O(1)이다.

```python
from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:    # skill_trees 반복
        is_possible = False     # is_possible 초기화
        
        # skill_routine, tree 모두 popleft 사용을 위해 deque 사용
        skill_routine = deque(skill)
        tree = deque(tree)
        
        # routine의 첫 번째 원소 꺼내기
        routine = skill_routine.popleft()

        while tree:
            now = tree.popleft()    # 첫 번째 tree 원소 값
            if routine == now:      # 원소가 같으면
                if not skill_routine:   # skill_routine이 남아 있지 않으면
                    is_possible = True      # is_possible에 True값 할당 후 종료
                    break
                routine = skill_routine.popleft()   # 남아 있으면 다음 routine 꺼내기
            
            elif now in skill_routine:  # tree 원소가 실행되기 전 선행되어야하는 것이 있을 경우 => 반복문 종료
                break      

            ### while 밖으로 뺐을 때,
            # skill_routine = 'BDE'
            # tree = 'BFE' 일때 문제가 생김
            if not tree:    # 더 이상 탐색할 tree가 없으면 종료
                is_possible = True
                break

        if is_possible:
            answer += 1

    return answer

```
