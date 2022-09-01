def solution(routes):
    answer = 1      # 첫 구간에 설치 가능한 카메라
    routes.sort()   #  정렬
    
    min_num, max_num = routes[0][0], routes[0][1]
    
    for route in routes:
        fr, to = route      # 현재 구간
            
        if min_num < fr:    # min_num과 max_num을 갱신해서 구간 좁히기
            min_num = fr
        if max_num > to:
            max_num = to
            
        if min_num > max_num:   # min_num이 max_num보다 커진다 => 구간 벗어남
            answer += 1             # 카메라 추가
            min_num, max_num = fr, to   # 다시 min_num, max_num 초기화
            
    return answer