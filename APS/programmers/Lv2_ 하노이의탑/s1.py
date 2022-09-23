def solution(n):
    answer = []

    def hanoi(depth, fr, to, mid):
        if depth == 1:
            answer.append([fr, to])
            return
        hanoi(depth-1, fr, mid, to)
        answer.append([fr, to])
        hanoi(depth-1, mid, to, fr)

    hanoi(n, 1, 3, 2)
    return answer