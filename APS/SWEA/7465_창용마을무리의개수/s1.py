import sys
sys.stdin = open('input.txt')

def find(x):
    if x == target_list[x]:
        return x
    else:
        return find(target_list[x])

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x > y:
        x, y = y, x

    target_list[y] = x
     
T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    target_list = [i for i in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    result_list = [find(i) for i in range(N+1)]
    result = set(result_list)

    print('#{} {}'.format(test, len(result)-1))