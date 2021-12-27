import sys
sys.stdin = open('input.txt')

sum_lst = [0] + [1] * (10**6 + 1)   # 0 ~ 10^6 크기 배열 초기화 (모두 1을 약수로 가지고 있기 떄문에 추가)
for ele in range(3, 10**6 + 1, 2):  # 3 ~ 10^6 까지의 홀수들을 반복하면서
    for idx in range(ele, 10**6 + 1, ele):  # sum_lst 배열에 ele만큼 차이나는 원소에 ele값 더하기(ele이 약수임을 의미)
        sum_lst[idx] += ele                 

### 시간초과 => 미리 합 계산하기
for idx in range(2, 10**6 + 1):     # 1 ~ R 까지의 합을 구하기 위해 더하기
    sum_lst[idx] += sum_lst[idx-1]

T = int(input())
for test in range(1, T+1):
    L, R = map(int, input().split())    

    # result = sum(sum_lst[L : R+1])
    result = sum_lst[R] - sum_lst[L-1]  # L ~ R까지의 합

    print('#{} {}'.format(test, result))
