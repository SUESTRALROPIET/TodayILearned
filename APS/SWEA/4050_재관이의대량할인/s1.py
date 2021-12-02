import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N = int(input())    # 사고자 하는 옷 개수
    prict_list = list(map(int, input().split()))    # 옷 가격 리스트
    prict_list.sort(reverse=True)   # 옷 가격 내림차순 정렬 

    result = 0
    idx = 0

    while idx < N:  # 옷 처음부터 끝까지 반복
        if idx % 3 == 2:    # 3번째 옷 값은 더하지 않고 continue
            idx += 1
            continue

        result += prict_list[idx]   # 옷 값 더하기
        idx += 1

    print('#{} {}'.format(test, result))