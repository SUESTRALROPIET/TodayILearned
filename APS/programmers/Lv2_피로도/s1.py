def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    checked = [0] * N   # 체크한 곳인지 확인하는 배열
    
    def dfs(step, total):   # 탐색한 던전 개수 기록, 현재 남은 피로도
        nonlocal answer
        if answer < step:   # 탐색한 던전 개수 & answer 비교 후 => 큰 수 반환
            answer = step
        for idx in range(N):    # 던전 모두 탐색
            if checked[idx]:        # 방문한 적 있으면 Pass
                continue       
            checked[idx] = 1        # 방문 체크
            if total-dungeons[idx][0] < 0:  # 갈 수 없는 던전이면 => 다른 던전 탐색
                dfs(step, total)
            else:
                dfs(step+1, total-dungeons[idx][1]) # 갈 수 있는 던전이면 => 던전 개수 기록 + 1, 피로도 계산
            checked[idx] = 0        # 방문 체크 해제
    
    dfs(0, k)
    
    return answer