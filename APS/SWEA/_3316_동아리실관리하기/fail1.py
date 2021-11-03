import sys
sys.stdin = open('input.txt')

def dfs(now_list, cnt):
    global result

    # 날짜가 채워지고, 조건을 통과해서 dfs로 돌아온 경우의 수 세기
    if cnt == len(manager_list):
        result += 1
        return

    # 모든 경우의 수 구하기
    for i in range(1, 1 << 4):
        temp_list = []
        for j in range(4):
            if i & (1 << j):
                temp_list.append(students[j])
        # 첫째날 (전날 이력이 없는경우) && 매니저 && A가 포함된 경우
        if cnt == 0 and (manager_list[cnt] in temp_list) and ('A' in temp_list):
            dfs(temp_list, cnt + 1)
        # 매니저 && 전날에 왔던 사람(키를 전달해 줄 수 있는 사람)이 있는 경우
        elif (manager_list[cnt] in temp_list) and (set(now_list) & set(temp_list)):
            dfs(temp_list, cnt + 1)

T = int(input())
for test in range(1, T+1):
    manager_list = list(input())
    students = ['A', 'B', 'C', 'D']
    result = 0

    dfs([], 0)
    print(result)
