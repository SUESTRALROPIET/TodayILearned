import sys
sys.stdin = open('input.txt')

def bfs(start_point, cnt):

    for next_point in range(101):
        if checked[next_point]:
            continue
        if contact[start_point][next_point] == 1:
            bfs(next_point, cnt+1)




# 인접행렬로 작성
for test in range(1, 11):
    N, start = map(int, input().split())
    contact_list = list(map(int, input().split()))
    contact = [[0] * 101 for _ in range(101)]
    checked = [0] * 101
    for idx in range(0, N, 2):
        contact[contact_list[idx]][contact_list[idx+1]] = 1

    checked[start] = 1
    result_cnt = 0
    result_node = 0
    bfs(start, 0)