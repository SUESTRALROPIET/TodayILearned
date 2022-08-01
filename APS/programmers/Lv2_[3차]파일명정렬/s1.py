import heapq

def solution(files):
    answer = []
    q = []
    
    for idx, file in enumerate(files):
        is_num = False

        head = ''
        num = ''
        
        for ele in file:         
            if is_num:                  # 현재 탐색구간: NUMBER
                if not ele.isnumeric():     # ele가 숫자가 아니면 => TAIL구간이므로 break
                    break
                
                num += ele                  # ele가 숫자면 => num에 ele 추가 후, continue
                continue
            
                                        # 현재 탐색구간: HEAD
            if ele.isnumeric():         # ele가 숫자면 => 탐색 구간 NUMBER로 변경 & num에 ele 추가
                is_num = True
                num += ele
                
            else:                       # ele가 숫자가 아니면 => head에 추가
                head += ele.upper()
                
        heapq.heappush(q, (head, int(num), idx, file))  # 정렬 순서: head > num > idx 순
    
    while q:
        a, b, c, d = heapq.heappop(q)
        answer.append(d)
        
    return answer
