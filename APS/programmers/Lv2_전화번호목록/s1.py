def solution(phone_book):
    def not_same(std, comp):
        idx = 0
        while idx < len(std):
            if std[idx] == comp[idx]:
                idx += 1
            else:
               return True
        return False
        
    answer = True
    N = len(phone_book)
    
    for i in range(N):
        i_len = len(phone_book[i])
        for j in range(i+1, N):
            j_len = len(phone_book[j])
            if i_len < j_len:
                answer = not_same(phone_book[i], phone_book[j])
            else:
                answer = not_same(phone_book[j], phone_book[i])
                
            if not answer:
                break
                
        if not answer:
                break
                
    return answer