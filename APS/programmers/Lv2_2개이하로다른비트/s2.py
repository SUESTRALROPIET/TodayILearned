def solution(numbers):
    answer = []

    for num in numbers:
        if num % 2 == 0:        # 숫자가 짝수이면 +1 이 답!
            answer.append(num + 1)
            continue
        
        # 숫자가 홀수이면, 2진수로 변환 후 팀색
        ## 1. 2짓수를 뒤에서부터 탐색해서 '0'이면, 0인 자릿수 ~ 그 다음 자리까지 => '10'으로 바꾸기
        ## 2. 만약에 2진수 수 안에 '0'이 없으면, 앞에 '1'을 붙여주고 + 가장 첫번째 자리는 '0'으로 바꿔주기
        bin_num = bin(num)
        idx = len(bin_num) - 1 
        while idx:
            if idx == 1:    # 2번 경우, '0'이 아예 없을 때
                f_num = '0b10' + bin_num[3:]
                answer.append(int(f_num, 2))
                break
            if bin_num[idx] == '0': # '0'을 찾았을 때
                f_num = bin_num[:idx] + '10' + bin_num[idx+2:]
                answer.append(int(f_num, 2))
                break
            idx -= 1

    return answer
