import sys
sys.stdin = open('input.txt')

def get_sum(num_lst):
    total_sum = 0
    for ele in num_lst:
        total_sum ^= ele
    
    return total_sum

T = int(input())
for test in range(1, T+1):
    N = int(input())                            # 사탕 봉지 개수 (2 <= N <= 1000)
    candy = list(map(int, input().split()))     # 각 사탕 봉지에 있는 사탕 수 (1 <= candy <= 1000000)

    candy_sum = get_sum(candy)
    result = 0

    for i in range(1, (1<<N)-1):
        my_candy = []
        for j in range(N):
            if i & (1 << j):
                my_candy.append(candy[j])
        
        if sum(my_candy) <= result:
            continue

        my_candy_sum = get_sum(my_candy)
        if my_candy_sum == candy_sum ^ my_candy_sum:
            if result < sum(my_candy):
                result = sum(my_candy)

    if not result:
        result = 'NO'
    
    print('#{} {}'.format(test, result))
    

