import heapq

def get_time(s, e):
    sH, sM = map(int, s.split(':'))
    eH, eM = map(int, e.split(':'))
    
    hour_diff = eH - sH
    min_diff = eM - sM
    
    if min_diff < 0:
        min_diff += 60
        hour_diff -= 1
    
    return (hour_diff * 60) + min_diff

def get_melody(time, std, melody):
    sharp_cnt = melody.count('#')
    melody_len = len(melody) - sharp_cnt
    share, remain = divmod(time, melody_len)

    whole_melody = melody * share + melody[:remain]
    remain_sharp_cnt = melody[:remain].count('#')
    
    if remain_sharp_cnt:
        whole_melody += melody[remain : remain + remain_sharp_cnt]
        remain += remain_sharp_cnt
        
    if remain and melody[remain] == '#':
        whole_melody += melody[remain]
    
    std_len = len(std)
    print(whole_melody)
    whole_melody_len = len(whole_melody)

    for start_idx in range(whole_melody_len):
        end_idx = start_idx + std_len
        if whole_melody[start_idx : end_idx] == std:
            if end_idx + 1 < whole_melody_len and whole_melody[end_idx] == '#': # 런타임 에러: 3, 4, 6, 8, 15, 18, 19 => 해결
                continue
            return True
    return False
        
def solution(m, musicinfos):
    q = []
    
    for idx, info in enumerate(musicinfos):
        start, end, title, melody = info.split(',')
        
        time = get_time(start, end)
        is_correct = get_melody(time, m, melody)
        
        if is_correct:
            heapq.heappush(q, (-time, idx, title))
    
    if q:
        answer = heapq.heappop(q)        
        return answer[-1]
    else:
        return "(None)"

print(solution("DF", ["6:20,6:50,TEST,DDF", "6:20,6:55,TEST2,DDF"]))