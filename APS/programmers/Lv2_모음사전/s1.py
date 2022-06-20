def solution(word):
    answer = 0
    
    cnt_dict = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    idx_dict = { 1: 781, 2: 156, 3: 31, 4: 6, 5: 1}
    
    idx = 0
    for ele in word:
        idx += 1
        answer += (cnt_dict[ele] * idx_dict[idx] + 1)
            
    return answer