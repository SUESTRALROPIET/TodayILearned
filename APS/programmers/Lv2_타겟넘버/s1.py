def solution(numbers, target):    
    answer = 0                      # 타겟 넘버가 되는 횟수 
    max_level = len(numbers)        # dfs 깊이: 리스트 길이
    
    def dfs(now_value, now_level):  # dfs(현재 값, 현재 level/깊이)
        
        if now_level == max_level:      # 모든 리스트 원소를 탐색했다면
            if now_value == target:         # target 값인지 확인 후 
                nonlocal answer                 # nonlocal: 가장 가까이서 둘러싸는 스코프에서 이미 연결된 변수를 가리킨다.
                answer += 1                     # answer에 횟수 1 더하기
            return
        
        for i in range(2):          # (0: 원소 빼기, 1: 원소 더하기)
            if i:
                dfs(now_value + numbers[now_level], now_level+1)
            else:
                dfs(now_value - numbers[now_level], now_level+1)
    
    dfs(0, 0)
        
    return answer