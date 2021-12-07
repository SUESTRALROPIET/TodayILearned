## 7465_창용 마을 무리의 개수

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWngfZVa9XwDFAQU
#### 1. [서로소 집합] find / union - set 활용

> - 상호배타집합 연산
>   - Make-Set(x) : 유일한 원소 x를 포함하는 새로운 집합을 생성하는 연산
>   - Find-Set(x) : x가 속한 대표원소 찾기
>   - Union(x, y) : x와 y의 대표원소를 합치기 
> - 마지막에 모든 원소의 부모찾는 find(x)를 해줘야 답이 나왔다.


```python
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
