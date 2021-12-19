## 3316_동아리실관리하기

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBnFuhqxE8DFAWr&categoryId=AWBnFuhqxE8DFAWr&categoryType=CODE&problemTitle=3316&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

#### ~~1. 가능한 모든 경우를 만든 후, 조건으로 걸러내기~~

> 시간 초과



#### 2. 경우의 수 계산하면서 풀기

> 매니저가 전날에 왔었다면 : `2 ** 3`
>
> 안왔다면, 매니저 제외, 온 사람(n) / 안 온사람 (m) : `(2 ** n - 1) * (2 ** m)`