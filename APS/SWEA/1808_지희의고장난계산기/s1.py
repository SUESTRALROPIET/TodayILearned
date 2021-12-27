import sys
sys.stdin = open('input.txt')

import itertools

def get_result(share, cnt):
    global min_result

    new_share = 0

    if test+1 == 8:
        pass
    for num in num_lst:
        if int(num) == 0 or int(num) == 1:
            continue

        if int(share) < int(num):
            continue

        if int(share) % int(num) == 0:
            new_share = str(int(share) // int(num))
            for ele in new_share:
                if ele in possible_num:
                    continue
                else:
                    return get_result(new_share, cnt+len(str(num))+1)
            
            result = cnt + len(new_share)+1 + len(str(num))+1   

            if result < min_result: # result가 min_result보다 작으면 반환
                min_result = result
                
            return                 
        
T = int(input())
for test in range(1, T+1):
    if test == 8:
        pass
    input_num = list(map(int, input().split()))     # (int) 0 ~ 9까지 가능 유무 => 1 / 0으로 이루어진 리스트
    target = input()                                # (str) 목표값
    N = len(target)                                 # 목표값 길이

    ### 누를 수 있는 숫자 possible_num에 담기
    possible_num = []                               # 가능한 숫자 담을 빈 리스트
    for idx in range(10):                           # idx: 0 > 9
        if input_num[idx]:                         
            possible_num.append(idx) 

    possible_num = list(map(str, possible_num))     # int > str 으로 변환하기

    get_comb = False        # get_comb 연산 여부 

    for target_ele in target:
        if target_ele in possible_num:  # target 숫자 모두 바로 누를 수 있으면
            continue
        else:                           # target 숫자 모두 바로 누를 수 없으면
            get_comb = True

    if get_comb:        # 바로 누를 수 없는 숫자는 조합을 조합하러 가기
        num_lst = []    # 가능한 조합을 담을 빈 리스트 초기화
        for i in range(N, 0, -1):     # N+1자리 ~ 1의 자리 숫자 조합
            num_lst += list(map(''.join, itertools.product(possible_num, repeat = i)))

                                                                                            # 중복 제거 후, 문자열인 숫자들을 정수형으로 바꿔줌
        num_lst = list(set(map(int, num_lst)))
        num_lst.sort(reverse=True)
        min_result = float('INF')   # 가장 적은 횟수를 담을 변수 초기화

        get_result(target, 0)

    else:
        min_result = N + 1  # target 숫자 길이 + 등호 연산자 개수 

    if min_result == float('INF'):  # min_result에 변화가 없으면 => 모든 수가 불가능함을 의미
        min_result = -1

    print('#{} {}'.format(test, min_result))
