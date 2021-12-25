# import sys
# sys.stdin = open('input.txt')

# # import itertools
# # possible_perm = list(itertools.permutations([1, 2, 3]))
# # print(possible_perm)

# def perm(arr, k):
#     global result
#     if k == N:
#         print(arr)
#     else:
#         for idx in range(N):
#             if not used[idx]:
#                 arr.append(input_lst[idx])
#                 used[idx] = 1
#                 perm(arr, k+1)
#                 arr.pop()
#                 used[idx] = 0

# T = int(input())
# for test in range(1, T+1):
#     N = int(input())
#     input_lst = list(map(int, input().split()))
#     used = [0] * N

#     left = right = 0
    
#     for idx in range(N):
#         used[idx] = 1
#         perm([input_lst[idx]], 1)
#         used[idx] = 0
        
N = 3
a = [1, 2, 3]
for i in range(1 << N):
    L_lst = []
    for j in range(N):
        if i & (1 << j):
            L_lst.append(a[j])
    print(L_lst)
