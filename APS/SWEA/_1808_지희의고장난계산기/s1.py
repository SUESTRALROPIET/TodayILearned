import sys
sys.stdin = open('input.txt')

T = int(input())
input_num = list(map(int, input().split()))
goal = int(input())
N = len(goal)

possible_num = []
num_lst = []

for idx in range(10):
    if input_num[idx]:
        goal % idx == 0
        possible_num.append(idx) 
        num_lst.append(idx)

print(possible_num)

