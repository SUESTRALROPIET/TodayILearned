import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):

    input_str = list(input())
    frog = ['c', 'r', 'o', 'a', 'k']    # 개구리 울음소리에 해당하는 문자열 리스트
    cnt_lst = [0, 0, 0, 0, 0]           # frog 원소 개수 기록하기

    result = 0      # 개구리 수 세기

    for ele in input_str:   # 주어진 input 문자열 끝까지 반복
        for frog_idx in range(5):   # 개구리 울음소리 길이만큼 반복: 0 -> 4
            if ele == frog[frog_idx]:   # input 문자열 원소가 frog 원소와 같다면
                if frog_idx == 0:           # 해당 원소의 idx가 0이면! 시작을 의미
                    if cnt_lst[4]:              # 울음을 다 끝낸 개구리가 있다면
                        for idx in range(5):        # cnt_lst의 모든 원소를 -1을 해준다.
                            cnt_lst[idx] -= 1
                        result = cnt_lst[0]         # 개구리 수 갱신: 결국 cnt_lst 첫번째값이 개구리 수가 됨.
                    cnt_lst[0] += 1             # ele의 idx값과 대응하는 cnt_lst 원소에 1 추가
                    result = cnt_lst[0]         # 개구리 수 갱신
                    break
                elif cnt_lst[frog_idx] < cnt_lst[frog_idx-1]:   # idx 1 ~ N-1: 앞 원소보다 현재 idx값이 작으면 가능한 울음소리 이므로
                    cnt_lst[frog_idx] += 1                          # ele의 idx값과 대응하는 cnt_lst 원소에 1 추가
                    break
                else:
                    result = -1     # 앞 원소보다 현재 idx값이 크면 => 불가능한 울음소리
                    break

        if result == -1:    # 위 반복문에서 나갈 수 있도록 추가
            break

    if cnt_lst[-1] != cnt_lst[0]:   # 첫번째 cnt값과 마지막 cnt값이 같지 않다면 => 불가능한 울음소리
        result = -1

    print('#{} {}'.format(test, result))