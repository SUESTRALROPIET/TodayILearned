def solution(phone_book):
    answer = True
    
    phone_book.sort()
    N = len(phone_book)
    
    for idx in range(N-1):
        std = phone_book[idx]
        comp = phone_book[idx+1]
        
        if std in comp:
            answer = False
            break
    
    return answer