## 4672_수진이의 팰린드롬

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWRKNev6fqYDFAV8
#### 1. 정렬된 문자열이 팰린드롬 최대값을 가진 문자열

> 문제의 예시에서 'abccba'일 경우 부분문자열이 팰린드롬인 경우의 수가 가장 많다고 하여, 정렬된 문자열이 부분문자열이 팰린드롬인 경우가 가장 많다는 것을 생각해내지 못했다.


```python
# 팰린드롬 단어인지 판별하는 함수
def is_palindrome(word):
    M = len(word)
    for idx in range(0, M//2):
        if word[idx] == word[M-1-idx]:
            continue
        else:
            return False
    return True

T = int(input())
for test in range(1, T+1):

    input_word = list(input())
    input_word.sort()       # input 단어 오름차순 정렬

    N = len(input_word)     # input 단어 길이 
    cnt = N                 # 길이가 1인 단어는 모두 팰린드롬이므로 > 단어 길이 카운트에 담고 시작

    now_len = 1         # 부부문자열 길이 
    while now_len < N:  # 부부문자열 길이가 N보다 작을때만 아래 코드 실행
        now_len += 1        # 부부문자열 길이 1씩 늘리기 
        for start_idx in range(0, N-now_len+1):     # 시작 인덱스: 0 -> input 단어길이-부분문자열길이
            if is_palindrome(input_word[start_idx:start_idx + now_len]):    # 팰린드롬인지 검사 후 > cnt에 1씩 더하기
                cnt += 1
    
    print('#{} {}'.format(test, cnt))