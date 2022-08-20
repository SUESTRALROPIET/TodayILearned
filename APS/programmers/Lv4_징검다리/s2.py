def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks.append(distance)
    
    min_dist = 0
    max_dist = distance
    
    
    while min_dist <= max_dist:
        now = 0
        mid = (min_dist + max_dist) // 2
        cnt = 0
        
        for rock in rocks:
            diff = rock - now
            if diff >= mid:     # 거리 mid가 최소값이 되어야하니까
                now = rock      # mid보다 큰 돌은 save, 작은 돌은 제거
            else:
                cnt += 1

        if cnt <= n:
            answer = mid        # [#추가 후, 해결!] answer값을 mid로 갱신
            min_dist = mid + 1
        else:
            max_dist = mid - 1
            
    return answer
