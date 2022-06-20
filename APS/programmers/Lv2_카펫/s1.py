def solution(brown, yellow):
    max_row = int(yellow ** 0.5)    # yellow의 제곱근 => 내림하기
    
    while max_row:
        share, remain = divmod(yellow, max_row)
        if remain == 0:     # 나누어 떨어지면
            cal = (share * 2) + (max_row * 2) + 4   # 해당 yellow 값에 대한 brown개수 계산해보기
            if cal == brown:                            # 계산한 brown 개수가 주어진 brown 개수와 동일하면
                answer = [share + 2, max_row + 2]       # yellow 가로/세로 기준, 가로/세로 길이 계산 (가로 >= 세로)
                break
        max_row -= 1        # max_row 하나씩 줄이며 탐색하기
    
    return answer