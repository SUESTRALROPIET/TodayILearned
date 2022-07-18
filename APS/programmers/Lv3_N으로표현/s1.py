def cal(a, b, ele):     # 사칙연산 계산
    if ele == '+':
        return a + b
    elif ele == '-':
        return abs(a - b)
    elif ele == '*':
        return a * b
    else:
        return a // b
    
def len_num(N, target_len): # target_len길이 만큼 N이어 붙이기
    N = str(N)
    N *= target_len
    return int(N)

def solution(N, number):
    def get_ele(num, chr_cnt):      # 1 ~ 8 길이의 사칙연산 모두 storage에 담기     
        for length in range(1, chr_cnt//2 + 1):
            if length == chr_cnt:
                new_num = len_num(num, chr_cnt)
                storage[chr_cnt].add(new_num)
                return
            
            a = len_num(num, length)
            b = len_num(num, chr_cnt - length)
            for ele in ele_lst:
                calculated = cal(b, a, ele)
                    
                if calculated:
                    storage[chr_cnt].add(calculated)
                    
        storage[chr_cnt].add(len_num(num, chr_cnt))

    ele_lst = ['+', '-', '*', '/']      # 사칙연산
    storage = [set() for _ in range(9)]     # 길이 8까지의 연산값 결과 저장하기

    for i in range(1, 9):
        get_ele(N, i)
        
    # 1 ~ 4까지 재탐색하여 2차 연산하기
    for i in range(1, 5):
        for j in range(8-i, 0, -1): # => 8-i ~ 1까지 재탐색 후, 1번 해결!
            for a in storage[i]:
                for b in storage[j]:
                    for ele in ele_lst:
                        calculated = cal(b, a, ele)
                        if calculated:
                            storage[i + j].add(calculated)
    
    # 주어진 값이 있으면 idx반환 / 없으면 -1 반환
    for idx in range(1, 9):
        if number in storage[idx]:
            return idx
    return -1
