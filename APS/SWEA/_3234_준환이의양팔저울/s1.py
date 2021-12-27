import sys
sys.stdin = open('input.txt')

import time
start = time.time()  # 시작 시간 저장

### 18개만 맞는 중...

# 오른쪽 추가 될 수 있는 모든 경우 반환하기 (부분집합)
def get_subset(arr):
    global sum_input

    result_lst = []
    for i in range(1 << N):
        subset_lst = []
        for j in range(N):
            if i & (1 << j):
                subset_lst.append(arr[j])
        
        right_sum = sum(subset_lst)
        left_sum = sum_input - right_sum
        if left_sum >= right_sum:       # 1. 시간 줄이기 1: 왼쪽 추 >= 오른쪽 추인 경우만 반환
            result_lst.append(subset_lst)
    
    return result_lst

# 순열 구하기 (추를 놓을 순서)
def perm(arr, k):
    global result
    if k == N:  # 모든 추를 다 놓았다면 => 가능한 경우인지 탐색하러 가기
        weighing(arr)
    else:
        for idx in range(N):
            if not used[idx]:
                arr.append(input_lst[idx])
                used[idx] = 1
                perm(arr, k+1)
                arr.pop()
                used[idx] = 0

# 순열대로 추를 놓았을 때 왼쪽 > 오른쪽이 유지되는지 탐색하기
def weighing(perm_lst):
    global cnt
    for right_perm in Right_lst:    # 오른쪽 추 리스트
        left = right = 0
        for ele in perm_lst:        # 순열 순서대로 저울에 놓으면서
            if ele in right_perm:   # 오른쪽 추 리스트에 속해있는 추면 => right에 추의 값 더하기
                right += ele
            else:                   # 아니면 => left에 추의 값 더하기
                left += ele

            if left < right:    # 계산 후, 왼쪽 < 오른쪽이면, break로 빠져나간 후 다른 경우 탐색
                break
            
            # if left >= (sum_input//2):
            #     cnt +=1 
            #     break
        else:                   # 조건을 모두 통과했으므로 경우의 수 cnt 1 증가
            cnt += 1

T = int(input())
for test in range(1, T+1):
    N = int(input())                            # 추 개수
    input_lst = list(map(int, input().split())) # 추 무게 리스트

    sum_input = sum(input_lst)      # 추 무게 총합
    cnt = 0                         # 조건에 맞는 경우의 수 세기

    Right_lst = get_subset(input_lst)   # 가능한 오른쪽 추 리스트
    
    # 순열 구하기
    used = [0] * N                              # 사용 유무
    for idx in range(N):
        used[idx] = 1
        perm([input_lst[idx]], 1)
        used[idx] = 0
        
    print('#{} {}'.format(test, cnt))


print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간