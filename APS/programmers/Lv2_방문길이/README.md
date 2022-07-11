## Lv.2 방문 길이

https://school.programmers.co.kr/learn/courses/30/lessons/49994

#### 1. 반복문 & 델타이동
> 시간 복잡도
> - dictionary 활용: O(1)
> - 리스트 자료형의 `append`: O(1)
> - 리스트 자료형의 `in`: O(N)

```python
def solution(dirs):
    answer = 0
    
    d = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}  # 방향코드에 따른 row, col 이동값
    pair = {'U': 'D', 'D': 'U', 'R': 'L', 'L': 'R'}     # 서로 반대방향 방향코드 pair 하기

    history = []    # 방문한 경로 저장
    row = col = 5   # 시작점: (0, 0) 대신 사용
        
    for dir in dirs:    # 주어진 방향값 반복
        ni = row + d[dir][0]
        nj = col + d[dir][1]

        if not (0 <= ni <= 10 and 0 <= nj <= 10):   # 범위 넘어가면 다음 방향 탐색
            continue
        
        if (ni, nj, dir) not in history:    # 방문한 적 있는지 검사
            history.append((ni, nj, dir))           # 추가원소 1: 새로운 위치 + 방향 
            history.append((row, col, pair[dir]))   # 추가원소 2: 현재 위치 + 방향
                
            answer += 1     # answer에 추가

        row = ni    # row, col 값 갱신
        col = nj
        
    return answer
```
