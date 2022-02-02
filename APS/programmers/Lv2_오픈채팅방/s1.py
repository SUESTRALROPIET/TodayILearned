def solution(record):
    
    answer = []                 # 정답 리스트 초기화
    user_nickname = dict()      # nickname 리스트 초기화
    
    massages_userId = []        # 출력할 메세지에 해당하는 userId 리스트 초기화
    messages = []               # 출력할 메세지 리스트 초기화
    
    for record_ele in record:   # input 리스트 전체 반복
        code, userId, *nickname = record_ele.split()    # code, userId, *nickname있으면 받기
        message = ''                                    # code별 메세지 초기화
        
        if code == 'Enter':                             # Enter
            user_nickname.update({userId : nickname})       # user_nickname 리스트에 userId & nickname update
            message = '님이 들어왔습니다.'                      

        elif code == 'Leave':                           # Leave
            message = '님이 나갔습니다.'
            
        elif code == 'Change':                          # Change
            user_nickname.update({userId : nickname})       # user_nickname 리스트에 userId & nickname update
            continue                                        # 다음 input 탐색
            
        massages_userId.append(userId)
        messages.append(message)
        
    for message_idx in range(len(messages)):
        result = user_nickname[massages_userId[message_idx]][0] + messages[message_idx]
        answer.append(result)
        
    return answer