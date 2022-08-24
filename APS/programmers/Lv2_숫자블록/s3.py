def get_num(num):   # 약수 중 최대값 구하기
    if num < 2:
        return 0
    m = int(num ** 0.5)
    for std in range(2, m+1):
        ans = num // std
        if num % std == 0:      ### 효율성 테스트 해결 포인트: 
            if ans < 10000000:  ### 몫이 블러 최대값 10000000을 넘을 수 없다.
                return num // std
    return 1

def solution(begin, end):
    answer = []
    
    for i in range(begin, end+1):
        answer.append(get_num(i))
    
    return answer