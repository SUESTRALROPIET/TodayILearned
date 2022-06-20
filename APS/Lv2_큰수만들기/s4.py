def solution(number, k):
    N = len(number)
    answer = ''
    idx = 0
    
    while idx < N-k and 0 < k:
        if number[idx] < number[idx+1]:
            number = number[:idx] + number[idx+1:]
            k -= 1
            idx = 0
        else: 
            idx += 1
    if k:
        number = number[:len(number)-k]

    answer = number
    
    return answer

k = solution("222", 1)

print(k)