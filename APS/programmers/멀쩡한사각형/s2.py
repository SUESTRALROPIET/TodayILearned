def solution(w,h):
    answer = 0

    if w == 1 or h == 1:        # w 또는 h가 1이면 => 0 반환
        return 0
    
    if w == h:                  # 정사각형이면 => 전체 칸 수 - 한 변 길이
        return (w * h) - w
         
    for row_idx in range(1, w+1):   # row_idx: 1 -> w
        cnt = -(h / w * row_idx) + h    # row_idx에 따른 y값을 기울기로 계산
        answer += int(cnt)              # 정수만 answer에 더하기

    return answer * 2           # 삼각형 2개 나오므로 2배 해주기

print(solution(8, 12))