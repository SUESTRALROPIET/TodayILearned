## 10816 숫자카드 2

https://www.acmicpc.net/problem/10816

#### 1. 딕셔너리 자료형 활용하기
> 시간 복잡도: O(N + M)
> - 이진탐색으로 푸는 방법 미해결
> - N: 카드 개수, M: 개수를 알아야하는 카드의 개수

```python
N = int(input())
cards = list(map(int, input().split()))
card_dict = dict()

# dictionary로 개수 저장
for card in cards:
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

M = int(input())
targets = list(map(int, input().split()))

# dictionary에서 개수 꺼내기
for target in targets:
    if target in card_dict:
        print(card_dict[target], end=" ")
    else:
        print(0, end=" ")
```

#### 2. 이진탐색으로 시작/끝 인덱스 구해서 풀시
```python
# 시작 인덱스 찾기
def lower(n):
    start = 0
    end = N - 1
    while start < end:
        mid = (start + end) // 2
        if n <= cards[mid]:
            end = mid
        else:
            start = mid + 1
    return end

# 끝 인덱스 찾기
def upper(n):
    start = 0
    end = N - 1
    while start < end:
        mid = (start + end) // 2
        if cards[mid] <= n :
            start = mid + 1
        else:
            end = mid
    return start

N = int(input())
cards = sorted(list(map(int, input().split())))

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    upper_idx = upper(target)
    lower_idx = lower(target)

    if upper_idx == N-1 and cards[N-1] == target:
        upper_idx += 1

    print(upper_idx - lower_idx, end=" ")
``` 