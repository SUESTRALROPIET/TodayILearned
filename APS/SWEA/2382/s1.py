import sys
sys.stdin = open('input.txt')

T = int(input())
N, M, K = map(int, input().split())

status_dict = dict()
new_status = dict()

direction = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(K):
    row, col, cnt, direction = map(int, input().split())
    if (row, col) in status_dict:
        status_dict[(row, col)].append((cnt, direction))
    else:
        status_dict[(row, col)] = [(cnt, direction)]

for group_idx, now_position in enumerate(status_dict):
    row, col = now_position
    a= status_dict[(row, col)]
