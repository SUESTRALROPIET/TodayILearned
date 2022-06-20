def solution(people, limit):
    answer = 0
    
    people.sort()
    
    while people:
        answer += 1
        now = people.pop()

        while people and people[0] <= limit - now:
            now += people.pop(0)
        
    return answer