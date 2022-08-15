def solution(order):
    answer = []

    N = len(order)
    boxes = [i for i in range(N, 0, -1)]
    sub = []

    idx = 0
    a = 0
    b = 0

    while idx < N:
        if boxes:
            a = boxes[-1]
        if sub:
            b = sub[-1]
        if boxes and order[idx] == a:
            boxes.pop()
            answer.append(a)
            idx += 1
            continue
        if sub and order[idx] == b:
            sub.pop()
            answer.append(b)
            idx += 1
            continue
        if boxes:
            sub.append(boxes.pop())
            continue
        break
    
    return len(answer)