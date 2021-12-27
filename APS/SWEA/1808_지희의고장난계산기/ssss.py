import sys
sys.stdin = open('input.txt')

# 피연산자가 3개 이상인 경우 X
import itertools

def get_result(num):
    global target, min_result

    if int(target) % int(num) == 0:     # 나머지 없이 나눠지게 되면
        share = str(int(target)//int(num))  # 몫의 숫자를 확인해서
        for ele in share:                   
            if ele in possible_num:         # 모두 누를 수 있는 숫자인지 확인
                continue
            else:                           # 아니라면 => return 
                return

        result = len(num) + len(share) + 2  # 모든 숫자가 있다면 => 각 숫자 길이 + 곱셈 + 등호 

        if result < min_result: # result가 min_result보다 작으면 반환
            min_result = result
        
T = int(input())
for test in range(1, T+1):
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

        min_result = float('INF')   # 가장 적은 횟수를 담을 변수 초기화

        for num in num_lst:     # 가능한 조합 리스트를 끝까지 탐색하며
            if int(num) == 0 or int(num) == 1:  # 0이나 1로 나눠진 결과값은 넘어가기
                continue

            if int(target) < int(num):  # target보다 큰 num은 넘어가기
                continue

            else:       # 가능한 수 버튼 누르는 횟수 계산하러 가기
                get_result(num)
    else:
        min_result = N + 1  # target 숫자 길이 + 등호 연산자 개수 

    if min_result == float('INF'):  # min_result에 변화가 없으면 => 모든 수가 불가능함을 의미
        min_result = -1

    print('#{} {}'.format(test, min_result))
