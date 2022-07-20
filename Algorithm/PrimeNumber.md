# 소수(Prime Number)
2보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로 나누어 떨어지지 않는 자연수


## 소수 판별하기
### 1. 어떤 수 X를 2부터 X-1 까지의 모든 수로 나누어보기
```python
  def is_prime_number(X):
    for i in range(2, X):
      if X % i == 0:
        return False
    return True
```
> 시간복잡도: O(X)

> 비효율적임

### 2. 어떤 수 X의 약수의 특징을 활용
> 특징: 가운데 약수를 기준으로 대칭되는 두 수를 곱하면 X가 나온다 => 즉, X의 제곱근까지만 확인하면 된다.

 ```python
    import math

    def is_prime_number(X):     # X**0.5 로 사용 가능 
      for i in range(2, int(math.sqrt(X) + 1)):
        if X % i == 0:
          return False
      return True
 ```
 > 시간복잡도: O(X^0.5)

### 3. 에라토스테네스의 체
> 여러개의 수가 소수인지 아닌지 판별할 때 사용하며, N보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있다.

#### 1. 알고리즘 원리
1. 2부터 N까지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. i를 제외한 남은 수 중에서 i의 배수를 모두 제거한다.
4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.

#### 2. 코드
```python
import math

N = 1000 
array = [True for i in range(N + 1)]  # 소수인지 기록하기

for i in range(2, int(math.sqrt(N) + 1)):   # i: 2 -> N ** 0.5
  if array[i] == True:  # i가 소수이거나 탐색한 적이 없으면,
    j = 2
    while i * j <= N:   # i를 제외한 i의 모든 배수 제거
      array[i * j] = False
      j += 1
```
> 시간복잡도: O(NloglogN) => 선형 시간에 동작할 정도로 빠름

> 단점: 메모리가 많이 필요하다.
 
> 에라토스테네스 체를 이용해야하는 문제의 경우 N이 1,000,000 이내로 주어지는 경우가 많다. 이는 이론상 400만 번 정도의 연산으로 문제를 해결할 수 있으며, 메모리 또한 충분히 처리할 수 있는 크기만큼만 차지한다.



