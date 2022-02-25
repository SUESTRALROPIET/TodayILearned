def solution(s):                                                                ## s: "{{20,111},{111}}"
    split_input = []    # 튜플 단위로 나누고 담기 위한 리스트 초기화
    s = s[2:-2].split('},{')    # 제일 바깥쪽 중괄호 제외하고! '},{' 기준으로 나눠 튜플 단위로 변환
                                                                                ## s: ['20,111', '111']
    for ele in s:       # 튜플을 반복하면서 ','단위로 나눠 set 형식으로 변환
        split_input.append(set(ele.split(',')))
                                                                                ## split_input: [{'20', '111'}, {'111'}]
    ordered_input = [set()] * (len(split_input) + 1)    # 각 튜플의 길이와 일치하는 idx번호에 튜플 담기
    for ele in split_input:
        ordered_input[len(ele)] = ele                                           ## ordered_input: [set(), {'111'}, {'20', '111'}]

    answer = []
    for idx in range(1, len(ordered_input)):                    # idx: 1 -> 튜플 전체 개수(ordered_input 길이)
        new_ele = ordered_input[idx] - ordered_input[idx-1]     # idx - (idx-1)에 해당하는 원소끼리 연산해서 유일하게 남는 값
        answer.append(new_ele.pop())                            # answer에 추가
    
    answer = list(map(int, answer))         # answer에 string으로 들어가 있는 원소들 숫자로 변환
    
    return answer


solution("{{20,111},{111}}")