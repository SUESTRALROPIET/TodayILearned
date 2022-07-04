## Lv.2 n^2 배열 자르기

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-Tj7ya3jYDFAXr&categoryId=AV-Tj7ya3jYDFAXr&categoryType=CODE&problemTitle=2930&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

#### 1. heapq 라이브러리 사용
> 시간복잡도: M * O(log N)
> - M: 명령어 길이
> - N: graph 길이

```python
import heapq

T = int(input())
for test in range(1, T+1):
    N = int(input())
    graph = []
    answer = []

    for _ in range(N):
        code, *num = map(int, input().split())
        if code == 1:
            heapq.heappush(graph, -num[0])
        elif graph:
            root_node = heapq.heappop(graph)
            answer.append(-root_node)
        else:
            answer.append(-1)

    print('#{}'.format(test), *answer)
```
#### 2. 리스트로 최대힙 구현(미완)