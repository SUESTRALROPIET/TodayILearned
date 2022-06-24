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