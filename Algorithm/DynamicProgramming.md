# 동적 프로그래밍(Dynamic Programming)
- [강의](https://www.youtube.com/watch?v=5Lu34WIx2Us)
- 재귀적으로 작성된 코드의 효율성을 높이는 방법
  1. 복잡한 문제를 재귀로 간단하게 표현 가능하나, 재귀는 종종 O(2^N)의 시간복잡도를 가진다.
  2. 재귀코드의 속도를 느리게 만드는 가장 큰 원인
      - 불필요한 재귀 호출
      - 하위 중첩 문제
      => 큰 문제와 작은 문제를 같은 방법으로 풀이하는 것이 가능하다. 작은 문제의 결과값이 항상 같다는 점을 이용하여 큰 문제를 해결하는 방식을 이용하기 때문이다. 또한 문제의 정답을 작은 문제의 정답에서 구할 수 있어야 한다. 따라서 정답을 구한 문제를 어딘가에 메모해 두고, 그보다 큰 문제를 풀게 되었을 경우 이전에 풀이했던 작은 문제의 결과값을 이용한다.

## 적용 조건
- 작은 문제에서 반복이 일어남
- 같은 문제는 항상 정답이 같음

## 재귀함수와 2가지 개선방법
- 하기 내용은 피보나치 수열을 활용하여 비교한 내용이다.
- 피보나치 수열(Fibonacci sequence)
    - 0과 1로 시작하며 이어지는 수는 수열의 앞 두 수의 합인 무한대로 이어지는 수학적 수열
    - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

### 0. 재귀함수
```python
def fib(n):
  if n == 0 or n == 1:
    return n

  return fib(n-2) + fib(n-1)
```
- 시간복잡도: O(2^N)

### 1. 메모이제이션(memoization) 기법 활용하기
```python
def fib(n, memo): # memo: 해시 테이블
  if n == 0 or n == 1:
    return n
  if n not in memo:
    memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
  
  return memo[n]
```
- 먼저 계산한 함수 결과를 기억해 재귀 호출을 감소시킴
- 시간복잡도: O(2N - 1) => O(N)

### 2. 상향식 기법 활용하기(반복문)
- 하위 문제를 중복 호출하지 않음
```python
def fib(n):
  if n == 0:
    return 0
   
  a = 0
  b = 1

  for i in range(1, n):
    temp = a
    a = b
    b = temp + a
  
  return b
```
- 시간복잡도: O(N)

### 메모이제이션 vs 상향식 기법
- 메모이제이션을 쓰더라도 재귀가 반복에 비해 오버헤드가 더 들기 때문에 재귀가 매우 직관적이지 않는 이상 상향식을 택하는 편이 낫다. 재귀를 어떻게 사용하든 컴퓨터는 호출 스택에 모든 호출을 기록해야 하므로 메모리를 소모한다. 메모이제이션 자체도 해시 테이블을 사용하므로 마찬가지로 컴퓨터 공간을 추가로 소모한다. 
- 재귀가 더 직관적이면 재귀를 사용하되 메모이제이션으로 빠르게 만들어야 한다.
- Top-Down 방식을 주로 이용하는 재귀와는 달리, DP에서는 Bottom-Up 방식을 이용한다.
    - 메모이제이션(memoization)(Top-Down): 하위 문제에 대한 정답을 계산했는지 확인해가면서 문제를 자연스러운 방식으로 풀어나간다.
    - 타뷸레이션(tabulation)(Bottom-Up): 더 작은 하위 문제부터 살펴본 다음, 작은 문제의 정답을 이용해 큰 문제의 정답을 풀어나간다.

## 시간 복잡도 공간복잡도
- 시간복잡도: O(N)

## 활용 문제
1. SWEA
    1. [SWEA - 5255. 타일 붙이기](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYNNbK29EDFAVT#)
    2. [SWEA - 5256. 이항계수](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYNNbK29EDFAVT#)
    3. [SWEA - 5258. 해피박스](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYNxvq3BIDFAVT)
    4. [SWEA - 5260. 부분 집합의 합](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYNxvq3BIDFAVT)
    5. [SWEA - 5262. 정렬된 부분 집합](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYODN63DsDFAVT)
    6. [SWEA - 5263. 그래프 최소 비용](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYODN63DsDFAVT)
    7. [SWEA - 5265. 전기카트 2](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYODN63DsDFAVT)
2. [프로그래머스 - 동적계획법](https://school.programmers.co.kr/learn/courses/30/parts/12263)
    1. [N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895)
    2. [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105)
    3. [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898)
    4. [도둑질](https://school.programmers.co.kr/learn/courses/30/lessons/42897)

## 관련 기술면접 질문
1. Dynamic Programming이란? 장점은?
    <details>
    <summary>답변</summary>
    <p>
      - 이전의 결과값들을 저장해서 처리 속도를 향상시키는 프로그래밍 기법
      - 큰 부분을 작은부분으로 분할해 문제를 해결, 작은 부분 중복해서해결함
      - * 분할/정복과 비슷하나 분할/정복은 작은 단위 문제로 나눴다가 다시 합병하며 해결하는 방법이고 동적 프로그래밍의 경우 작은 문제가 반복하여 일어난다. 이 작은 문제들의 결과값은 항상 같은데 이 값을 저장해놓고 이용한다(Memorization). 같은 문제의 답은 항상 같다. 가장 대표적인 예로 피보나치 수열이 있다.
    </p>
    </details>
2. Dynamic Programming과 분할정복의 차이점은?
    <details>
    <summary>답변</summary>
    <p>
    </p>
    </details>
3. Dynamic Programming 적용 조건
    <details>
    <summary>답변</summary>
    <p>
    </p>
    </details>
4. Dynamic Programming 활용 예시
    <details>
    <summary>답변</summary>
    <p>
        강화학습, NLP에 있어서 DP의 문제 해결방식은 큰 도움을 준다.
    </p>
    </details>

## 참고 자료
- [누구나 자료구조와 알고리즘](http://www.yes24.com/Product/Goods/61941073)
- [알고리즘 - Dynamic Programming(동적프로그래밍)이란?](https://galid1.tistory.com/507)