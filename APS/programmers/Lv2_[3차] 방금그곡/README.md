## Lv.2 [3차] 방금그곡

https://school.programmers.co.kr/learn/courses/30/lessons/17683

#### 1. heapq(최대힙 & 최소힙) + idx, 반복문으로 # 추가 처리
> - 런타임 에러: 3, 4, 6, 8, 15, 18, 19 번
>
>   => `end_idx + 1 < whole_melody_len` 로 해결
> - 실패: 12
> 
>   =>  해결 못함

### 2. heapq(최대힙 & 최소힙) + `in` 연산자
> - `'#' => 소문자로 변환`하는 아이디어 다른 풀이 참고 후 해결

```python
import heapq

def convert_sharp(str):     # '#' => 소문자로(string) 변환하기
    return_lst = []
    for ele in str:
        if ele == '#':
            pre = return_lst.pop()
            converted = chr(ord(pre) + 32)
            return_lst.append(converted)
        else:
            return_lst.append(ele)
    return ''.join(return_lst)

def get_time(s, e):     # 재생된 시간(분) 반환하기
    sH, sM = map(int, s.split(':'))
    eH, eM = map(int, e.split(':'))
    
    hour_diff = eH - sH
    min_diff = eM - sM
    
    if min_diff < 0:
        min_diff += 60
        hour_diff -= 1  # 0에서 1로 변경 => 27번 해결
    
    return (hour_diff * 60) + min_diff

def get_melody(time, std, melody):
    melody_len = len(melody)
    share, remain = divmod(time, melody_len)
    whole_melody = melody * share + melody[:remain]

    if std in whole_melody:
        return True
    else:
        return False
        
def solution(m, musicinfos):
    m = convert_sharp(m)
    q = []
    
    for idx, info in enumerate(musicinfos):
        start, end, title, melody = info.split(',')
        melody = convert_sharp(melody)
        
        time = get_time(start, end)
        is_correct = get_melody(time, m, melody)
        
        # -time: 최대힙
        # idx: 최소힙
        if is_correct:
            heapq.heappush(q, (-time, idx, title))
    
    if q:
        answer = heapq.heappop(q)        
        return answer[-1]
    else:
        return "(None)"
```