# 순열과 조합, 중복순열과 중복조합

## 순열(Permutation)
> 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것 (순서 O, 중복 X)
> 
> nPr = n! / (n - r)!
1. 재귀
    ```python
        data = [1, 2, 3, 4]
        N = 4       # 데이터 총 길이
        repeat = 3  # 반복할 횟수

        answer = [0] * repeat   # 순열을 담을 리스트
        visited = [False] * N   # 방문 체크

        get_permutation(0)
    ```
    ```python
        def get_permutation(now):

            if now == repeat:
                print(answer)
                return 
                
            for idx in range(N):

                if visited[idx]:
                    continue

                visited[idx] = True
                answer[now] = data[idx]

                get_permutation(now+1)

                visited[idx] = False
    ```

2. 라이브러리
    ```python
      from itertools import permutations

      data = [1, 2, 3, 4]

      for x in permutations(data, repeat): # repeat개를 선택(순서 O)
        print(x)
    ```

## 조합(Combination)
> 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것 (순서 X, 중복 X)
> 
> 
1. 재귀
    ```python
        data = [1, 2, 3, 4]
        N = 4
        repeat = 3

        visited = [False] * N
        answer = [0] * repeat

        get_combination(0, 0)
    ```
    ```python
        def get_combination(now_idx, now):
            
            if now == repeat:
                print(answer)
                return

            for idx in range(now_idx, N):

                if visited[idx]:
                    continue

                visited[idx] = True
                answer[now] = data[idx]
                
                get_combination(idx, now+1)

                visited[idx] = False
    ```
    > 순열에서 사용하지 않던 `now_idx` 추가로 활용하여 어떤 원소를 기준으로 다음 원소를 탐색할지 기록 및 전달함

2. 라이브러리
    ```python
      from itertools import combinations

      data = [1, 2, 3]

      for x in combinations(data, repeat): # repeat개 선택(순서 X)
        print(x)
    ```

## 중복 순열
> 서로 다른 n개에서 중복이 가능하도록 r개를 선택하여 일렬로 나열하는 것 (순서 O, 중복 O)
1. 재귀
    ```python
        data = [1, 2, 3, 4]
        N = 4       # 데이터 총 길이
        repeat = 3  # 반복할 횟수 or 중복 횟수

        answer = [0] * repeat   # 순열을 담을 리스트
        visited = [0] * N   # 방문 체크 + 반복 횟수 체크

        get_permutation_with_repetition(0)
    ```
    ```python
        def get_permutation_with_repetition(now):

            if now == repeat:
                print(answer)
                return 
                
            for idx in range(N):

                if visited[idx] == repeat:
                    continue

                visited[idx] += 1
                answer[now] = data[idx]

                get_permutation_with_repetition(now+1)

                visited[idx] -= 1
    ```

2. 라이브러리
    > `product(반복 가능한 객체, repeat=반복횟수)`
    ```python
        from itertools import product

        for x in product([1, 2, 3, 4], repeat=3):
            print(x)
    ```

## 중복 조합
> 서로 다른 n개에서 순서에 상관없이 r개를 중복이 가능하도록 선택하는 것 (순서 X, 중복 O)

1. 재귀
    ```python
        data = [1, 2, 3, 4]
        N = 4       # 데이터 총 길이
        repeat = 3  # 반복할 횟수 or 중복 횟수

        answer = [0] * repeat   # 조합을 담을 리스트
        visited = [0] * N   # 방문 체크 + 반복 횟수 체크

        get_combination_with_repetition(0, 0)
    ```
    ```python
        def get_combination_with_repetition(now_idx, now):
            
            if now == repeat:
                print(answer)
                return

            for idx in range(now_idx, N):

                if visited[idx] == repeat:
                    continue

                visited[idx] += 1
                answer[now] = data[idx]
                
                get_combination_with_repetition(idx, now+1)

                visited[idx] -= 1
    ```

2. 라이브러리
    > `combinations_with_replacement(반복 가능한 객체, r(반복 횟수))`
    ```python
        from itertools import combinations_with_replacement

        for x in combinations_with_replacement([1,2,3], 2):
            print(x)
    ```

## 참고 자료
- [이것이 취업을 위한 코딩 테스트다](http://www.yes24.com/Product/Goods/91433923)