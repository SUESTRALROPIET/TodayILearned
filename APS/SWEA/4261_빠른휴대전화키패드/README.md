## 4261_빠른 휴대전화 키패드
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWLL7kaaAPsDFAUW&categoryId=AWLL7kaaAPsDFAUW&categoryType=CODE&problemTitle=4261&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

#### 1. 키패드를 딕셔너리로 초기화해서 사전단어 숫자로 변환
```python
# 숫자와 해당 숫자에 포함된 문자들 dict 형태로 담기
keypad_dict = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'], 
    '5': ['j', 'k', 'l'], 
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}
T = int(input())
for test in range(1, T+1):
    input_str, N = input().split()
    words = list(input().split())

    cnt = 0     # 유효한 단어 개수 cnt 초기화

    for word in words:  # 사전 단어를 반복하면서
        temp_str = ''       # 변환된 숫자를 담아줄 문자열 초기화
        for ele in word:        # 각 단어의 알파벳을 반복하면서
            for keypad in keypad_dict:  # keypad를 반복하면서
                if ele in keypad_dict[keypad]:  # 해당 숫자의 value값에 알파벳이 있으면
                    temp_str += keypad      # 문자열에 key값 추가
                    break
            if temp_str == input_str:   # 만들어진 문자열이 주어진 input_str과 같으면 cnt++
                cnt += 1    

    print('#{} {}'.format(test, cnt))
```