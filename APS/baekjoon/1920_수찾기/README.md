## 1920 수 찾기

https://www.acmicpc.net/problem/1920

#### 1. 이진 탐색
> 시간 복잡도: O(log N)

```python
    def binary_search(num):
        start = 0
        end = N-1
        while start <= end:
            mid = (start + end) // 2
            
            if num == A[mid]:
                return print(1)
            elif num < A[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return print(0)

    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    M = int(input())
    target_lst = list(map(int, input().split()))

    for target in target_lst:
        binary_search(target)
```