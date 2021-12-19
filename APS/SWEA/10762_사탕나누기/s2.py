import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))

    total = 0               # 0 초기화
    for num in num_lst:     # 모든 수 XOR 연산
        total ^= num
    
    # 모든 수를 XOR연산했을 때,
    # 0이 나오면 => 어떤 수를 XOR연산을 해도 어떤 수와 같은 값이 나온다. 
    #       => 공평하게 나눌 수 있음 => 가장 적게 든 사탕을 동생에게 주면 해결!
    if total:
        result = 'NO'
    else:
        result = sum(num_lst) - min(num_lst)
    
    print('#{} {}'.format(test, result))
