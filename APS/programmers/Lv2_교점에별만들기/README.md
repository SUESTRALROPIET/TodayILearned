## Lv.2  교점에 별 만들기

https://programmers.co.kr/learn/courses/30/lessons/87377

#### 1. 이중 for문으로 전체 탐색하기
> 시간복잡도: O(n**2)
> 
> - 선들의 교차점을 모든 선들을 반복하면서 찾아냄
> - 주어지는 선의 최대길이는 1000이기 때문에 최악의 경우 시간 복잡도는 999000이 됨

```python
def solution(line):
    container = []  # . 으로 초기화된 2차원 배열
    points = []     # 별 좌표를 담는 배열
    
    N = len(line)
    for a in range(N-1):
        A, B, E = line[a]
        for b in range(a+1, N):
            C, D, F = line[b]
            
            divisor = (A * D) - (B * C)
            if divisor:
                x, x_remain = divmod((B * F) - (E * D), divisor)
                y, y_remain = divmod((E * C) - (A * F), divisor)
                if x_remain == 0 and y_remain == 0:     # 나머지가 없는 경우(정수) points에 추가
                    points.append((x, y))

    points.sort()   # x기준으로 정렬
    min_x = points[0][0]    # x의 최소값 뽑기
    x_width = abs(points[0][0] - points[-1][0]) # 가로 길이
    points.sort(key = lambda x: -x[1])  # y기준으로 정렬
    max_y = points[0][1]    # y의 최대값 뽑기
    y_width = abs(points[0][1] - points[-1][1]) # 세로 길이
    
    for _ in range(y_width + 1):    # x축, y축 때문에 1만큼 큰 넓이/높이 container 만들기
        container.append(['.'] * (x_width + 1))
    
    # 변환해서 '*' 찍어주기
    for point in points:
        x, y = point
        x, y = abs(y - max_y), abs(x - min_x)
        container[x][y] = '*'
    
    answer = []
    for row in container:
        answer.append(''.join(row))

    return answer
```