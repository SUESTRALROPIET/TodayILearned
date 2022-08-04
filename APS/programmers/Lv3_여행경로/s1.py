from collections import deque

# BFS
def solution(tickets):  
    answer = []    
    N = len(tickets)
    q = deque([(["ICN"], [])])
    
    while q:
        history, visited = deque.popleft(q)
        now = history[-1]       # 현재 위치
        
        if len(visited) == N:   # 모든 티켓 방문했으면 탐색 종료
            answer.append(history)
            continue

        for idx, ticket in enumerate(tickets):  # 티켓 전체 탐색
            fr, to = ticket
            
            if idx in visited:      # 방문한적 있으면 continue
                continue
            if now != fr:           # 출발지가 현재 위치와 다르면 continue
                continue

            deque.append(q, (history+[to], visited+[idx]))  # 새로운 지역 & 방문체크

    answer.sort()   # 정렬 후 첫번째 배열값 반환
    return answer[0]
