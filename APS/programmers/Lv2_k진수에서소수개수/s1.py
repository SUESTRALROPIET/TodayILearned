def convert(num, std):      # std진수로 변환 후, '0' 기준으로 split
    str_num = ''
    
    while num:
        str_num = str(num%std) + str_num
        num //= std
        
    return str_num.split('0')

def is_prime(n):    # prime number인지 검사
    n = int(n)
    if n < 2:
        return False
    m = int(n ** 0.5)
    i = 2
    while i <= m:
        if n % i == 0:
            return False
        i += 1
    return True
    
def solution(n, k):
    answer = 0
    converted = convert(n, k)

    for ele in converted:
        if not ele.isnumeric():
            continue
        if is_prime(ele):
            answer += 1
        
    return answer