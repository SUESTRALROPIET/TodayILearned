## 3459. 승자 예측하기
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWFPoj1qANoDFAV0

### 1. ~~다음에 올 경우의 수 예측하여 풀기~~
> 48479개 맞음
```python
T = int(input())
for test in range(1, T+1):
    N = int(input())

    now_num = 1
    cnt = 0

    while now_num <= N:
        cnt += 1

        if 2 ** (cnt+1) <= N < 2 ** (cnt+2):
            now_num = (now_num * 2) + 1
        else:
            now_num *= 2

    if (cnt-1) % 2:
        winner = 'Alice'
    else:
        winner = 'Bob'

    print('#{} {}'.format(test, winner))
```
### 2. 다음에 올 경우의 수 예측하여 풀기
```python
T = int(input())
for test in range(1, T+1):
    N = int(input())            # 주어진 값에서 2단계 전을 예상해서 빼 나가는 것이 핵심! 

    while 3 < N:
        N = N//2 + 1
        N = N//2 - 1

    if N == 1:
        result = 'Bob'
    else:
        result = 'Alice'

    print('#{} {}'.format(test, result))
```
