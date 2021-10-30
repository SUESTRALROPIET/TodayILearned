import sys
sys.stdin = open('input.txt')

for test in range(1, 11):
    N = int(input())
    input_list = list(input())

    # 괄호 짝 만들기
    op_dict = {'(' : ')', '{' : '}', '[' : ']', '<' : '>'}

    # 짝이 없는 괄호들 담아줄 stack 초기화
    stack = []

    # 입력값이 남아있으면 while이하 실행
    while input_list:
        ele = input_list.pop(0)         # ele는 input 첫번째 인덱스 값
        if ele in list(op_dict.keys()): # ele 이 열린 괄호이면, stack에 추가 
            stack.append(ele)
        elif op_dict[stack[-1]] == ele: # ele이 닫힌 괄호이면, 
            stack.pop()                 # stack의 마지막 값과 비교하여 짝이 맞으면 pop! 
        else:                           # 짝이 맞지 않으면 반복문 끝내기
            break
    
    if input_list:      # 입력값이 남아있으면 유효 X
        result = 0
    else:               # 입력값 모두 검사를 완료했으면 유효 O
        result = 1
    
    print('#{} {}'.format(test, result))
