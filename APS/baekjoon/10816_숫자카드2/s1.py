import sys
sys.stdin = open('input.txt')

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
