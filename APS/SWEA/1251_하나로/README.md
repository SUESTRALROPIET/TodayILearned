## 1251_하나로
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV15StKqAQkCFAYD&categoryId=AV15StKqAQkCFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=2
> 프림 알고리즘 또는 크루스칼 알고리즘으로 해결해야하는데 기억이 나질 않아 찾아서 해결했다

#### 1. 크루스칼 알고리즘
> 찾아보기 전에 해결하지 못했다
>
> 서로소 집합개념부터 복습이 필요하다!

```python
def find_set(x):        # 루트 노드 번호 찾기
    if x == make_set[x]:
        return x
    else:
        return find_set(make_set[x])

def kruskal(weight_list):   
    global result

    for weight in weight_list:  # 정렬된 가중치리스트를 반복하면서
        a, b, w = weight

        if find_set(a) != find_set(b):  # 루트 노드번호가 다르면 
            result += w                     # result에 가중치 w 더하기
            make_set[find_set(b)] = find_set(a) # a와 b 루트 노드 번호 기록하기

T = int(input())
for test in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))    
    E = float(input())

    node_list = []  # 주어진 노드 좌표 담기
    for idx in range(N):
        node_list.append((x_list[idx], y_list[idx]))

    weight_list = []    # 가중치 값을 담아줄 리스트 준비
    
    for start in range(N-1):    # 노드들을 반복하면서 가중치 계산하기
        start_x, start_y = node_list[start]
        for end in range(start+1, N):
            end_x, end_y = node_list[end]
            weight_list.append((start, end, (start_x-end_x)**2 + abs(start_y-end_y)**2))

    weight_list.sort(key=lambda x:x[2]) # 가중치 기준으로 오름차순 정렬

    make_set = [i for i in range(N)]    # 루트 노드번호 초기화
    result = 0                          # 가중치 결과값

    kruskal(weight_list)

    print('#{} {}'.format(test, round(result*E)))
```



#### 2. 프림 알고리즘

> 해결하지 못함
