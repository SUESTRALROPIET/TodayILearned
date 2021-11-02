import sys
sys.stdin = open('input.txt')

def bfs(now_x, now_y, cnt):


T = int(input())
for test in range(1, 2):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]

    bfs(0, 0, 0)
