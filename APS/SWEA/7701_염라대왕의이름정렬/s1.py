import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N = int(input())                        # 단어 개수
    name_lst = [set() for _ in range(51)]   # 0 ~ 50 길이이 단어들을 담을 set으로 구성된 배열
    for _ in range(N):                          # 단어 개수만큼 반복하면서
            input_str = input()                     # input 문자열
            input_len = len(input_str)              # 문자열 길이
            name_lst[input_len].add(input_str)      # set에 문자 담기

    print('#{}'.format(test))       # test case 출력
    for lst_idx in range(51):       # 단어 길이 0~50까지 모두 탐색하면서
        if name_lst[lst_idx]:           # 만약 해당 idx에 단어가 있으면
            result_lst = list(name_lst[lst_idx])    # set -> list로 변환후
            result_lst.sort()                       # 정렬
            M = len(result_lst)
            for ele_idx in range(M):                # 해당 idx 배열의 길이만큼 반복하면서 모든 단어 출력
                print(result_lst[ele_idx])
