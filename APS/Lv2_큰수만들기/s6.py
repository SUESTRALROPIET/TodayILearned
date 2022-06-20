def solution(number, k):
    idx = 0
    while idx < len(number)-1 and 0 < k:
        if number[idx] < number[idx+1]:
            number = number[:idx] + number[idx+1:]
            k -= 1
            if idx > 0:
                idx -= 2    # 왜 0부터 계산하지 않는지?
            else:
                idx -= 1
        idx += 1

    if k:
        number = number[:len(number) - k]

    answer = number
    return answer

answer = solution("22222", 4)
print(answer)