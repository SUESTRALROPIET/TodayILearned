'''
* 최대공약수(GCD) 함수
: 최대공약수를 중 가장 큰 수를 반환주는 함수
: Return the greatest common divisor of the specified integer arguments.
(예) gcd(10, 100) = 10

* 최소공배수(LCM) = 두 자연수의 곱 / 최대공약수
'''
from math import gcd

def solution(arr):      
    answer = arr[0]
    for n in arr:
        answer = n * answer // gcd(n, answer)

    return answer