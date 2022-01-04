import sys
sys.stdin = open('input.txt')

def find_set(num):                      # 부모 번호를 찾는 함수
    while status[num] != num:

        # return find_set(status[num])   # ==>  시간초과 원인

        # 이하 시간 초과 해결 방법
        status[num] = find_set(status[num])
        return status[num]
        
    return num 

def union(num1, num2):                  # 합집합 함수
    if status[num2] != num1:
        status[find_set(num2)] = find_set(num1)

T = int(input())
for test in range(1, T+1):    
    N, M = map(int, input().split())

    status = [i for i in range(N+1)]    # 각자의 인덱스 번호로 부모번호 초기화

    result = ''

    for j in range(M):
        code, a, b = map(int, input().split())

        if code:                            # code가 1이면, a, b가 같은 그룹인지 검사
            if find_set(a) != find_set(b):
                result += '0'
            else:
                result += '1'

        else:                               # code가 0이면, a, b 합집합 연산
            union(a, b)
        
    print('#{} {}'.format(test, result))