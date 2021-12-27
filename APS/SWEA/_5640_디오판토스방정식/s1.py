import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):
    a, b, c = map(int, input().split())
    