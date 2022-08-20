def solution(distance, rocks, n):    
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
            if diff >= mid:
                now = rock
            else:
                cnt += 1

        if cnt <= n:
            min_dist = mid + 1
        else:
            max_dist = mid - 1
            
    return mid
