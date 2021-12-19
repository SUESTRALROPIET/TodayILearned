import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    str_num = input()   # 입력값
    cnt = 0             # 횟수 

    while 1 < len(str_num):     # str_num 길이가 2 이상일때만 실행
        new_num = str(int(str_num[0]) + int(str_num[1]))    # 첫번째/두번째 숫자 합해서
        str_num = new_num + str_num[2:]                     # 기존 문자열 앞에 붙이기
        cnt += 1                                            # 횟수 추가
    
    if cnt % 2:     # cnt가 홀수이면 => A / 아니면 => B가 승리!
        winner = 'A'
    else:
        winner = 'B'

    print('#{} {}'.format(test, winner))
        