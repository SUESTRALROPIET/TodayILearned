import sys
sys.stdin = open('input.txt')

import heapq

T = int(input())
for test in range(1, T+1):
    N = int(input())
    graph = []
    answer = []

    for _ in range(N):
        code, *num = map(int, input().split())
        if code == 1:   # 최대힙 원소 추가
            heapq.heappush(graph, -num[0])
        elif graph:     # 루트값 반환
            root_node = heapq.heappop(graph)
            answer.append(-root_node)
        else:           # 빈 그래프일 경우
            answer.append(-1)

    print('#{}'.format(test), *answer)


