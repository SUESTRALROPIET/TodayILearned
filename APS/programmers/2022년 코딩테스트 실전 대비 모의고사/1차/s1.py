def solution(X, Y):
    answer = ''

    X = list(X)
    Y = list(Y)
    X.sort()
    Y.sort()

    x_idx = len(X) - 1
    y_idx = len(Y) - 1

    while 0 <= x_idx and 0 <= y_idx:
        if X[x_idx] == Y[y_idx]:
            answer += X[x_idx]
            x_idx -= 1
            y_idx -= 1
        elif X[x_idx] > Y[y_idx]:
            x_idx -= 1
        else:
            y_idx -= 1

    if answer:
        A = len(answer)
        if A == answer.count("0"):
            return "0"
        return answer
    return "-1"