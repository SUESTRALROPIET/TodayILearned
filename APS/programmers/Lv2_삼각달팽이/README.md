## Lv.2 삼각 달팽이

https://programmers.co.kr/learn/courses/30/lessons/68645

#### 1. 각 변에 따라 for문 작성
> 반시계방향으로 회전하는 수는 n번이기 때문에, step만큼 반복하면서 배열을 채움
> 채워지는 배열의 col값은 가장 앞 또는 가장 뒤이기 때문에, front & back 변수 추가 활용

```python 
def solution(n):
    triangle = []
    for i in range(1, n+1):
        triangle.append([0] * i)

    # col값 (front: 가장 앞 / back: 가장 뒤)
    front = 0
    back = -1
    
    k = -1  # 방향 (k % 3 => 0: 아래로, 1: 오른쪽으로, 2: 윗쪽으로)
    ni = nj = -1    # ni, nj 초기값

    num = 0 # 배열에 담을 숫자

    for step in range(n, 0, -1):    # step: n -> 1
        k += 1
        calK = k % 3
        if calK == 0:
            for _ in range(step):
                ni += 1     # row값: 증가
                nj = front  # col값: 가장 앞
                num += 1    # 담을 숫자

                triangle[ni][nj] = num

            front += 1  # col값: 가장 앞 숫자 1 증가

        elif calK == 1:
            for _ in range(step):
                nj += 1     # col값: 증가
                num += 1    # 담을 숫자

                triangle[ni][nj] = num

        elif calK == 2:
            for _ in range(step):
                ni -= 1     # row값: 감소
                nj = back   # col값: 가장 뒤
                num += 1    # 담을 숫자

                triangle[ni][nj] = num

            back -= 1  # col값: 가장 뒤 숫자 1 감소

    
    answer = []
    for ele in triangle:
        answer += ele

    return answer
```
