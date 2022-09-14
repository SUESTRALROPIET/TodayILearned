## Lv.2 행렬의 곱셈

https://school.programmers.co.kr/learn/courses/30/lessons/12949

#### 1. 반복문 (w. zip 함수)
> 시간복잡도: O(N*M)
>   -  N: arr1 길이, M: arr2 길이

```python
    def solution(arr1, arr2):
        answer = []
        
        # arr2 방향 전환
        rotated_arr2 = []
        arr_row = len(arr2)
        arr_col = len(arr2[0])
        col = 0
        while col < arr_col:
            new_ele = []
            for row in range(arr_row):
                new_ele.append(arr2[row][col])
            rotated_arr2.append(new_ele)
            col += 1
        
        # arr1 & arr2 행렬곱셈
        for ele1 in arr1:
            new_lst = []
            for ele2 in rotated_arr2:
                ans = 0
                for a, b in zip(ele1, ele2):
                    ans += a * b
                new_lst.append(ans)
            answer.append(new_lst)
        
        return answer
```