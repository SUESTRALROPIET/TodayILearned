## 1238. Contact

https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV15B1cKAKwCFAYD&categoryId=AV15B1cKAKwCFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=2

#### 1. 인접 리스트로 간선 표현 + bfs 하기

```python
def bfs(now_node, cnt):
    global result_cnt, result_node

    if result_cnt < cnt:
        result_cnt = cnt
        result_node = now_node
    elif result_cnt == cnt:
        if result_node < now_node:
            result_node = now_node

    for node_num in contact_list[now_node]: # contact_list에 담긴 노드들 모두 반복
        if not checked[node_num]:                   # 아직 연락이 안된 사람이면
            checked[node_num] = 1                   # 연락 체크
            checked_list.append((node_num, cnt))    # checked_list에 (노드번호, 횟수) 담기
    while checked_list:                     # check_list가 존재하면 아래 명령문 실행
        next_node, cnt = checked_list.pop(0)    # pop해서 다음 연락자 탐색
        bfs(next_node, cnt+1)

for test in range(1, 11):
    N, start = map(int, input().split())
    input_list = list(map(int, input().split()))
    contact_list = [[] for _ in range(101)] # 각 인덱스에는 해당 인덱스에서 연락이 닿을 수 있는 노드 번호들이 담김
    for idx in range(0, N, 2):
        contact_list[input_list[idx]].append(input_list[idx+1])

    checked_list = []   # 연락이 닿은 사람들의 (노드번호, 횟수)가 담김

    checked = [0] * 101 # 연락 된 사람들 체크
    checked[start] = 1  # 출발 노드번호 연락 체크

    # 결과값
    result_cnt = 0  # 연락 횟수
    result_node = 0 # 노드 번호

    bfs(start, 1)   # start 노드번호부터 시작! 

    print('#{} {}'.format(test, result_node))
```

#### 2. 인접 행렬로 간선 표현 + dfs 하는 방법으로 해결 X

> dfs로 해결하려다 보니 결과값을 제대로 찾지 못했다.

