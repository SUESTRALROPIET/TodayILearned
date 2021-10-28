import sys
sys.stdin = open('input.txt')

for test in range(1, 11):
    N = int(input())
    input_list = list(map(int, input().split('+')))
    print('#{} {}'.format(test, sum(input_list)))