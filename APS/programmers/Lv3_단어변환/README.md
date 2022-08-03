## Lv.3 단어 변환

https://school.programmers.co.kr/learn/courses/30/lessons/43163

#### 1. DFS + visited 배열
> 시간복잡도: O(N * N-1 * N-2 * ... * 2 * 2) = O(N^2)

 ```python
    def solution(begin, target, words):
        def get_check(fst, scd):    # 현재 단어(fst)에서 바꿀수 있는 단어(scd)인지 체크
            diff = 0
            fst = list(fst)
            scd = list(scd)

            for idx in range(M):
                if fst[idx] != scd[idx]:
                    diff += 1
                if 1 < diff:        # 알파벳 2개이상 다르면 FALSE: 바꿀 수 없음
                    return False
            return True
            
        def dfs(now, cnt):
            nonlocal answer
            
            if answer <= cnt:   # 현재 cnt가 answer보다 크면 더 이상 탐색X
                return
            
            if now == target:   # 현재 단어가 target과 동일하면: answer 비교 후 갱신하기
                if cnt < answer:
                    answer = cnt
                return

            for idx in range(N):        # words단어 탐색하기
                if checked[idx]:                # checked 배열: 탐색한 적이 있으면 더 이상 방문 X
                    continue
                if get_check(now, words[idx]):  # 탐색 가능한 단어이면: 체크 > dfs > 체크 풀기
                    checked[idx] = 1
                    dfs(words[idx], cnt+1)
                    checked[idx] = 0
        
        if target not in words:     # target이 배열 words안에 없으면 0 반환
            return 0
        
        answer = 50
        N = len(words)  # words 배열 길이
        M = len(begin)  # 주어진 단어 길이
        
        checked = [0] * N
        dfs(begin, 0)
        
        return answer
 ```