def solution(topping):
    N = len(topping)
    answer = 0

    for idx in range(1, N):
        left = len(set(topping[:idx]))
        right = len(set(topping[idx:]))

        if left == right:
            answer += 1

    return answer