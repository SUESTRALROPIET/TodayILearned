# 시간초과: 11 / 12 / 14

def solution(w,h):
    answer = 0

    for row_idx in range(1, w+1):
        cnt = -(h / w * row_idx) + h
        answer += int(cnt)
    return answer * 2


print(solution(8, 12))
print(solution(499, 27))
print(solution(499, 1000))