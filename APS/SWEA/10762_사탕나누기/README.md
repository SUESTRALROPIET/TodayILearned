## 10762_사탕나누기

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXSVhGoqED8DFAQT

#### ~~1. 전체합 ^ 부분집합의 합 XOR연산해서 구하기~~

> 시간 초과

```py
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
```



#### 2. 전체 합이 0이면, 가장 적은 사탕봉지를 동생에게 주면 됨!

> - 전체 합이 0일때, 어떤 수를 XOR연산하든 동일한 값이 나온다.

 ```python
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
 ```

