a = [1, 2, 3]
# for i in range(1 << 3):
#     print(i)
for i in range(1 << 3): 
    temp = ''
    print(i, '|', end='')
    for j in range(i):
        if i & (1 << j):
            temp = '1' + temp
        else:
            temp = '0' + temp
    print('%6s' % (temp))