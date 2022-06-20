## Lv.2 영어 끝말잇기

https://programmers.co.kr/learn/courses/30/lessons/12981

#### 1. 주어진 배열 반복하면서 검사하기
```python 
def solution(n, words):
    completed = []  # word 이력
    time = 0    # 횟수
    player = 0  # 플레이어 번호
    status = '' # 상태

    while words:
        time += 1   # 횟수 1 추가
        for i in range(1, n+1): # i(플레이어번호): 1 -> n
            if not words:   # 반복할 단어 있는지 체크부터하기
                status = 'break'
                break
            word = words.pop(0) # 단어 하나 뽑고
            player = i          # 플레이어 번호 기록
            if completed and word[0] != completed[-1][-1]:  # 올바른 끝말잇기 단어인지 체크
                status = 'break'    # 아니면 => 'break'
                break
            if word in completed:   # 이미 언급된 단어인지 체크
                status = 'break'
                break
            completed.append(word)  # 모든 조건 통과시 completed에 단어 추가하기

        if status == 'break':
            break
    
    if status != 'break' and not words: # 'break' 없이 모든 단어를 반복했을 때 (탈락자 없음) 
        return [0, 0]

    return [player, time]
```
