def solution(s):
    stack = []

    for ele in s:                           # input값 s 끝까지 탐색
        if len(stack) and stack[-1] == ele:     # stack에 쌓인 원소가 있고 /and/ input원소가 stack 가장 위에 있는 원소와 같다면
            stack.pop()                             # stack에서 제거
        else:
            stack.append(ele)                       # stack에 추가

    if stack:       # stack에 남아 있는 원소가 있으면 => 0 반환
        return 0
    else:           # 없으면 => 1 반환
        return 1