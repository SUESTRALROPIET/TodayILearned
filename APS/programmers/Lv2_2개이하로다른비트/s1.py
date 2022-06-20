def solution(numbers):
    answer = []
    
    for num in numbers:
        compare_num = num + 1
        while True:
            xor_num = num ^ compare_num
            diff_cnt = 0
            while xor_num:
                if xor_num % 2:
                    diff_cnt += 1
                    if 2 < diff_cnt:
                        break
                xor_num //= 2             
            if 2 < diff_cnt:
                start_num += 1
            else:
                break   
        answer.append(compare_num)
    return answer