def solution(record):
    
    answer = []
    user_nickname = dict()
    
    massages_userId = []
    messages = []
    
    for record_ele in record:
        code, userId, *nickname = record_ele.split()
        message = ''
        
        if code == 'Enter':
            user_nickname.update({userId : nickname})
            message = '님이 들어왔습니다.'

        elif code == 'Leave':
            message = '님이 나갔습니다.'
            
        elif code == 'Change':
            user_nickname.update({userId : nickname})
            continue 
            
        massages_userId.append(userId)
        messages.append(message)
        
    for message_idx in range(len(messages)):
        result = user_nickname[massages_userId[message_idx]][0] + messages[message_idx]
        answer.append(result)
        
    return answer