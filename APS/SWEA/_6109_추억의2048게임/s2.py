import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    N, S = input().split()
    N = int(N)

    matrix = [list(map(int, input().split())) for _ in range(N)]