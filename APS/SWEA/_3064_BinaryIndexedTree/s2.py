import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    input_lst = [0] + list(map(int, input().split()))

