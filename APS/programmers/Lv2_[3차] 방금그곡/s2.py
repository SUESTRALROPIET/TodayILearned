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
