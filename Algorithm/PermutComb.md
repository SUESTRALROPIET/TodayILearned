# 순열과 조합
## 순열(Permutation)
> - 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것 (순서 O)
> 
> - nPr = n! / (n - r)!
1. 재귀
    ```python
    ```
2. 반복문
    ```python
    ```
3. 라이브러리
    ```python
      import itertools

      data = [1, 2]

      for x in itertools.permutations(data, 2): # 2개를 선택(순서 O, 중복 허용)
        print(list(x))
    ```

## 조합(Combination)
> 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것 (순서 X)
> 
> 
1. 재귀
    ```python
    ```
2. 반복문
    ```python
    ```
3. 라이브러리
    ```python
      import itertools

      data = [1, 2, 3]

      for x in itertools.combinations(data, 2): # 2개 선택(순서 X, 중복 X)
        print(list(x))
    ```