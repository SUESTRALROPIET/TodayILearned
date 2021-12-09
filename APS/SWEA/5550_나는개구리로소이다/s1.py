import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):

    input_str = list(input())
    frog = ['c', 'r', 'o', 'a', 'k']

    input_idx = 0
    frog_idx = 0

    cnt = 1

    while input_str:    # input 문자열 반복하면서
        if frog_idx == 5:   # frog_idx가 끝까지 가면 다시 0으로 초기화
            frog_idx = 0

        if len(input_str) <= input_idx: # input문자열 끝까지 검사했으면
            if frog_idx == 0:       # frog idx가 초기화된 상태(frog idx 반복이 끝났다는 것을 의미)이면,
                input_idx = 0           # input idx 초기화해서 다시 처음부터 검사하고
                cnt += 1                # 개구리 수 추가
            else:
                cnt = -1            # 모두 해당되지 않으면 불가능한 울음소리 이므로 -1 반환후 반복문 종료
                break


        input_ele = input_str[input_idx]
        frog_ele = frog[frog_idx]

        if input_ele == frog_ele:   # input/frog 문자열이 동일하면 input 문자열 pop해서 제거 후
            input_str.pop(input_idx)
            frog_idx += 1           # 다음 frog 문자 탐색
        else:
            input_idx += 1          # 아니면 다음 input문자열 탐색

    if frog_idx != 5:   # 모두 반복이 끝났는데 frog_idx가 5가 아니면 => 불가능한 울음소리이므로 -1 반환
        cnt = -1

    print('#{} {}'.format(test, cnt))