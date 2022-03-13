def solution(name):   
    name_len = len(name)
    cnt_lst = [0] * name_len

    for idx in range(name_len):
        fst = 26 + ord('A') - ord(name[idx])
        scd = ord(name[idx]) - ord('A')
        cnt_lst[idx] = min(fst, scd)

    answer = sum(cnt_lst) + name_len - 1
        
    return answer

# print(solution("ABAAAAAAAAABB"))
# print(solution("JAN"))