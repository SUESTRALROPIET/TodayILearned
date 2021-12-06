import sys
sys.stdin = open('input.txt')

def find(x):
    if x == target_list[x]:     # 본인이 부모이면 본인 return
        return x
    else:                       # 아니면 부모 찾아서 return
        return find(target_list[x])

def union(x, y):
    target_list[find(y)] = find(x)  # y에 x의 부모 담기

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    target_list = [i for i in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
        # print(target_list)

    result_list = [find(i) for i in range(N+1)]
    result = set(result_list)

    print('#{} {}'.format(test, len(result)-1))