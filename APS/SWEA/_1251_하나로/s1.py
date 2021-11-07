import sys
sys.stdin = open('input.txt')

def get_min_result(now):
    global result, cnt

    if cnt == N-1:
        return 

    visited[now] = 1

    temp_node = 0
    temp_result = float('INF')

    for next_node in range(N):
        if not visited[next_node]:
            if matrix[now][next_node] < temp_result:
                temp_node = next_node
                temp_result = matrix[now][next_node]
    cnt += 1
    result += matrix[now][temp_node]
    get_min_result(temp_node)

T = int(input())
for test in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))    
    E = float(input())

    node_list = []
    for idx in range(N):
        node_list.append((x_list[idx], y_list[idx]))

    visited = [0] * N

    matrix = [[0] * N for _ in range(N)]
    
    for start in range(N-1):
        start_x, start_y = node_list[start]
        for end in range(start+1, N):
            end_x, end_y = node_list[end]
            matrix[start][end] = matrix[end][start] = (start_x-end_x)**2 + abs(start_y-end_y)**2
    
    cnt = 0
    result = 0

    get_min_result(0)        

    print('#{} {}'.format(test, round(result*E)))
