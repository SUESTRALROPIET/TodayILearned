def solution(phone_book):
    answer = True
    
    phone_book.sort()   # phone_book 정렬
    N = len(phone_book)
    
    for idx in range(N-1):
        std = phone_book[idx]
        comp = phone_book[idx+1]
        
        if std == comp[:len(std)]:  # std 길이 만큼 comp 앞부분과 비교
            answer = False
            break
    
    return answer