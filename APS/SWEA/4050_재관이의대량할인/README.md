## 4050_재관이의 대량 할인

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIseXoKEUcDFAWN&categoryId=AWIseXoKEUcDFAWN&categoryType=CODE&problemTitle=4050&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

#### 1. 입력값 내림차순 정렬 후, 3번째 옷값은 계산하지 않고 continue

 ```python
 T = int(input())
 for test in range(1, T+1):
     N = int(input())    # 사고자 하는 옷 개수
     prict_list = list(map(int, input().split()))    # 옷 가격 리스트
     prict_list.sort(reverse=True)   # 옷 가격 내림차순 정렬 
 
     result = 0
     idx = 0
 
     while idx < N:  # 옷 처음부터 끝까지 반복
         if idx % 3 == 2:    # 3번째 옷 값은 더하지 않고 continue
             idx += 1
             continue
 
         result += prict_list[idx]   # 옷 값 더하기
         idx += 1
 
     print('#{} {}'.format(test, result))
 ```

