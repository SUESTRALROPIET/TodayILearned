def solution(people, limit):
    answer = 0  # 구명보트 왕복 횟수
    
    people.sort()   # 무게 정렬
    
    N = len(people) # 사람 전체 수
    start = 0   # 제일 작은 무게 idx값
    end = N-1   # 제일 무거운 무게 idx값
    
    while start <= end: # 시작/끝 idx가 겹치지 전까지 반복
        answer += 1         # 구명보트 횟수 추가
        now = people[end]   # 현재 구명보트에 포함된 무게
        end -= 1            # 끝 idx 조절

        while start <= end and people[start] <= limit - now:    # 더 실을 수 있는지 체크
            now += people[start]    # 가장 작은 무게 채울 수 있으면 채우고, 
            start += 1              # 시작 idx 조절
        
    return answer