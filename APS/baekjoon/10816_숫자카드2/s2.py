import sys
sys.stdin = open('input.txt')

# 시작 인덱스 찾기
def lower(n):
    start = 0
    end = N - 1
    while start < end:
        mid = (start + end) // 2
        if n <= cards[mid]:
            end = mid
        else:
            start = mid + 1
    return end

# 끝 인덱스 찾기
def upper(n):
    start = 0
    end = N - 1
    while start < end:
        mid = (start + end) // 2
        if cards[mid] <= n :
            start = mid + 1
        else:
            end = mid
    return start

N = int(input())
cards = sorted(list(map(int, input().split())))

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    upper_idx = upper(target)
    lower_idx = lower(target)

    if upper_idx == N-1 and cards[N-1] == target:
        upper_idx += 1

    print(upper_idx - lower_idx, end=" ")
