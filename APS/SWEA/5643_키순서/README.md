## 5643_키 순서

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXQsLWKd5cDFAUo&categoryId=AWXQsLWKd5cDFAUo&categoryType=CODE&problemTitle=%ED%82%A4+%EC%88%9C%EC%84%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

#### 1. dfs로 탐색하면서 set 합연산 하기

> 좀 오래 걸리는 단점이 있다.

 ```python
 def get_smaller_set(input_list):
     global smaller_set
     for ele in input_list:          # 리스트를 반복하면서 
         if not smaller_check[ele]:      # 체크한 적 없는 학생이면
             smaller_check[ele] = 1          # 체크하고
             smaller_set |= set(smaller_list[ele])   # 작은 학생 기존 set에 합연산
             get_smaller_set(smaller_list[ele])      # dfs로 끝까지 탐색
 
 def get_bigger_set(input_list):
     global bigger_set
     for ele in input_list:
         if not bigger_check[ele]:
             bigger_check[ele] = 1
             bigger_set |= set(bigger_list[ele])
             get_bigger_set(bigger_list[ele])
 
 T = int(input())
 for test in range(1, T+1):
     N = int(input())    # 전체 학생 수
 
     smaller_list = [[] * (N+1) for _ in range(N+1)] # idx보다 작은 사람 리스트
     bigger_list = [[] * (N+1) for _ in range(N+1)]  # idx보다 큰 사람 리스트
     
     M = int(input())    # 명시된 키 비교 개수
     for _ in range(M):
         a, b = map(int, input().split())
         smaller_list[b].append(a)   # idx보다 작은 사람 리스트에 담기
         bigger_list[a].append(b)    # idx보다 큰 사람 리스트에 담기
 
     result = 0  # 결과값 
     
     for idx in range(1, N+1):   # 1번 학생부터 N번 학생까지 반복
         smaller_check = [0] * (N+1)     # 체크한 학생인지 기록하기
         bigger_check = [0] * (N+1)
 
         smaller_set = set(smaller_list[idx])    # 해당 idx보다 작은 학생 리스트 > set 로 변경
         bigger_set = set(bigger_list[idx])      # 해당 idx보다 큰 학생 리스트 > set 로 변경
 
         get_smaller_set(smaller_list[idx])  # dfs로 smaller_set에 idx보다 작은 학생 추가로 담기
         get_bigger_set(bigger_list[idx])    # dfs로 bigger_set에 idx보다 큰 학생 추가로 담기
 
         if len(smaller_set) + len(bigger_set) == N-1:   # smaller_set과 bigger_set 길이 합이 (전체학생수-1)이면
             result += 1                                 # result에 카운트하기 (몇번째 키 인지 명확한 학생)
 
     print('#{} {}'.format(test, result))
 ```



