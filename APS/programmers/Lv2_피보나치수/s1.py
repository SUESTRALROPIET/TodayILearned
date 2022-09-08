MAX_NUM = 100001
fibo = [0 for _ in range(MAX_NUM)]
fibo[0] = 0
fibo[1] = 1
for i in range(2, MAX_NUM):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % 1234567
    
def solution(n):
    return fibo[n]