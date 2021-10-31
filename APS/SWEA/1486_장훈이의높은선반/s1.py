import sys
# import time

# start = time.time() 
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N, B = map(int, input().split())    # 직원 수 / 최소 값
    num_list = list(map(int, input().split()))  # 직원 키 리스트

    result = float('INF')   # 결과값(최소값) 초기화

    # 부분집합의 합 구하기
    for i in range(1, 1 << N):
        temp_result = 0     # 임시 합계
        for j in range(N):
            if i & (1 << j):
                temp_result += num_list[j]
        # 부분집합의 합이 B(기준값)이상이고, result보다 작으면 => result값 갱신
        if B <= temp_result and temp_result < result: 
            result = temp_result
            
    print('#{} {}'.format(test, result - B))

# print("time :", time.time() - start)