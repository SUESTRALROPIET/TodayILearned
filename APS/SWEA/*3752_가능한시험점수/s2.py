import sys
sys.stdin = open('input.txt')      

T = int(input())
for test in range(1, T+1):
    N = int(input())
    score_lst = list(map(int, input().split()))

    max_sum = sum(score_lst)            # 모든 문제를 맞혔을 때 값
    check_score = [0] * (max_sum + 1)   # 나올 수 있는 점수를 체크할 리스트 초기화
    check_score[0] = 1                  # 모두 틀렸을 때 => 0점이 나오므로 체크 

    for score in score_lst:             # 모든 문제 반복
        for check_idx in range(max_sum, -1, -1):    # check_idx: max_sum -> 0   
                                                    ## check_idx: 0 -> max_sum 으로 하면 안됨
            if check_score[check_idx]:              ## 큰 점수부터 반복하면서 점수 더하기 
                check_score[check_idx+score] = 1    ## 나올 수 있는 점수 체크

    result = sum(check_score)   # 체크된 개수 구하기

    print('#{} {}'.format(test, result))
