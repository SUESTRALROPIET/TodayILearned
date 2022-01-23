def solution(w,h):
    answer = 0

    if w == 1 or h == 1:
        return 0
    
    if w == h:
        return (w*h) - w
         
    for row_idx in range(1, w+1):
        cnt = -(h / w * row_idx) + h
        answer += int(cnt)

    return answer * 2

print(solution(12, 8))
print(solution(8, 12))
print(solution(3, 3))
print(solution(499, 27))
print(solution(1000, 499))
print(solution(499, 1000))