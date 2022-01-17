import sys
sys.stdin = open('input.txt')

def dfs(q_num, score):
    if q_num == N:
        possible_score.add(score)
        return
    dfs(q_num+1, score+score_lst[q_num])       
    dfs(q_num+1, score)       

T = int(input())
for test in range(1, T+1):
    N = int(input())
    score_lst = list(map(int, input().split()))
    possible_score = set()

    dfs(0, 0)
    
    result = len(possible_score)
    print('#{} {}'.format(test, result))
