def solution(n,a,b):    
    answer = 0

    gap = 2     # 초기 구간값
    same_part = True    # a, b 모두 같은 구간에 있을때까지

    while same_part:
        for i in range(1, n+1, gap):    # i: 1 -> n
            if i <= a < i + gap and i <= b < i + gap:   # a 와 b 모두 같은 구간에 있게 되면
                same_part = False                       # same_part 변수 False로 변경
                break
        answer += 1     # 구간에 포함되지 않을 경우 answer에 1씩 더해줌 (대결 수)
        gap *= 2        # gap 도 2를 곱해주어 2의 제곱으로 늘려줌

    return answer

print(solution(8, 4, 7))
