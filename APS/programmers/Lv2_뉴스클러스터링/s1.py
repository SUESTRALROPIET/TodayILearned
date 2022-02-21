def solution(str1, str2):
    def make_lst(input_str):
        return_lst = []
        N = len(input_str)
        for input_idx in range(N-1):
            if input_str[input_idx:input_idx+2].isalpha():
                return_lst.append(input_str[input_idx:input_idx+2].upper())
        return return_lst

    str1_lst = make_lst(str1)
    str2_lst = make_lst(str2)
    
    compare1 = []   # 다중집합 교집합
    compare1_1 = [] 
    compare2 = []   # 다중집합 합집합
    compare2_1 = []

    compare1_1 += str2_lst
    compare2 += str1_lst
    compare2_1 += str1_lst

    for str1_ele in str1_lst:
        if str1_ele in compare1_1:
            compare1.append(str1_ele)
            compare1_1.remove(str1_ele)         # 추가: 4, 7, 9, 10, 11 틀림

    for str2_ele in str2_lst:
        if not str2_ele in compare2_1:
            compare2.append(str2_ele)
        else:
            compare2_1.remove(str2_ele)
    
    try:
        answer = len(compare1) / len(compare2) * 65536
    except:
        answer = 1 * 65536

    return int(answer)


print(solution('a', 'b'))


