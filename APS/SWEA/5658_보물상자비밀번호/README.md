## 5658_보물상자 비밀번호

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo&categoryId=AWXRUN9KfZ8DFAUo&categoryType=CODE&problemTitle=5658&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

#### 1. 한 변 문자열 길이에 따라 문자열 변환 + 가능한 숫자 set으로 담아서 풀기

 ```python
 T = int(input())
 for test in range(1, T+1):
     N, K = map(int, input().split())    # 총 숫자 개수 / K번째로 큰 수 구하기
     M = N // 4                          # 한 변에 있는 숫자 개수
 
     input_str = input()     # 주어진 숫자 문자열
 
     possible_set = set()    # 나올 수 있는 숫자 set
 
     for start_idx in range(M):  # 시작 인덱스: 0 -> M-1 (한변크기 만큼 돌아가면 초기 숫자열과 동일)
         rotate_str = input_str[start_idx:] + input_str[:start_idx]
 
         for split_idx in range(0, N-M+1, M):    # 돌렸을 때 한 변에 있을 수 있는 숫자 개수만큼 끊어서 
             possible_set.add(rotate_str[split_idx:split_idx+M]) # possible_set에 담기
 
     possible_lst = list(possible_set)   # possible_set > 리스트로 변환
     possible_lst.sort(reverse=True)     # possible_lst 내림차순으로 정렬하고
 
     result = int(possible_lst[K-1], 16) # K번째로 큰 16진수 수 10진수로 변환 :) 
 
     print('#{} {}'.format(test, result))
 
 ```



