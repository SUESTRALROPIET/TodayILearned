from collections import deque

def solution(cacheSize, cities):
    cities = list(map(lambda x: x.upper(), cities))
    answer = 0
    
    q = deque([])
    
    for city in cities:
        if cacheSize == 0:
            answer = len(cities) * 5
            break

        if len(q) < cacheSize:
            q.append(city)
            answer += 5
            continue

        if city in q:
            q.remove(city)
            q.append(city)
            answer += 1
        else:
            q.popleft()
            q.append(city)
            answer += 5    

    return answer

k = solution(3, ["A","B","A"])
print(k)