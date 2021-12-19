## 3378_스타일리쉬 들여쓰기

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWD3nB5q3T0DFAUZ

#### 1. 가능한 R, C, S 가능한 조합 완전탐색!!!

> 아이디어 힌트 얻고 출발~
>
> 1. `1 <= R, C, S <= 20` 제한된 조건 안에서 가능한 조합 모두 탐색하기
> 2. 가능한 조합들을 바탕으로 필요한 결과값 구하기
>
> 
>
> - 모든 조합을 탐색해서 정답을 좁혀나가는 것을 생각하지 못했다.
> - 조건을 어떻게 줘야할지 고민하는 시간이 길었다.

```python
def get_comb(r, c, s, dot_cnt):     
    global comb_lst

    # 들여쓰기 횟수에 맞는 R / C / S 조합 possible_comb 리스트에 담기
    possible_comb = []
    for possible_r in range(1, 21):
        for possible_c in range(1, 21):
            for possible_s in range(1, 21):
                if (r * possible_r) + (c * possible_c) + (s * possible_s) == dot_cnt:
                    possible_comb.append((possible_r, possible_c, possible_s))

    # comb_lst가 이미 있으면, 
    # 기존 comb_lst와 possible_comb리스트의 교집합 부분 반환
    if comb_lst:
        comb_lst = list(set(comb_lst) & set(possible_comb))
    else:
        comb_lst = possible_comb

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())

    comb_lst = []       # 가능한 R / C / S 조합 담을 리스트 초기화

    r, c, s = 0, 0, 0       # r, c, s 모두 0으로 초기화
    dot_cnt = 0             # 들여쓰기 수 
    couting_dot = False     # 들여쓰기가 아직 안 끝났으면 False / 끝났으면 True

    for _ in range(N):          # 들여쓰기를 파악할 수 있는 주어진 문장 N개
        couting_dot = False     # 문장이 시작할때마다 => 들여쓰기 세기 위한 설정
        input_line = input()    # 주어진 문장

        for ele in input_line:  # 문장의 요소(ele)들을 탐색
            if not couting_dot and ele == '.':      # 들여쓰기가 아직 안 끝나고 / 요소가 '.'이면
                dot_cnt += 1                        # 들여쓰기 세기
                continue

            couting_dot = True      # '.' 이 더이상 아니면 들여쓰기가 끝났으므로 => True
            if dot_cnt and couting_dot:     # 들여쓰기 수가 존재하며(첫문장처럼 들여쓰기가 없을때는 함수 실행X) / 들여쓰기가 끝났으면
                get_comb(r, c, s, dot_cnt)  # 함수 실행
                dot_cnt = 0                 # 들여쓰기 수 초기화

            # 이하 괄호 개수 세기
            if ele == '(':
                r += 1
            elif ele == ')':
                r -= 1
            elif ele == '{':
                c += 1
            elif ele == '}':
                c -= 1
            elif ele == '[':
                s += 1
            elif ele == ']':
                s -= 1

    # ---------------------------------
    # 주어진 문장에 알맞은 들여쓰기 횟수 계산하기
    # ---------------------------------
    r = c = s = 0   # 괄호 횟수 초기화
    result = [0]    # 들여쓰기 횟수 값 담기 (첫문장은 무조건 0)

    for output_idx in range(M):     # 주어진 문장 M개
        output_str = input()

        # 괄호 개수 기록하기
        for ele in output_str:
            if ele == '(':
                r += 1
            elif ele == ')':
                r -= 1
            elif ele == '{':
                c += 1
            elif ele == '}':
                c -= 1
            elif ele == '[':
                s += 1
            elif ele == ']':
                s -= 1
        
        # 필요한 괄호 계산하기
        if r == c == s == 0:    # 괄호가 필요 없는 문장이면 => 0   --없으면 2개가 틀림
            result.append(0)

        elif comb_lst:          # comb_lst에 가능한 R/C/S 조합이 있으면 
            for ele in comb_lst:    # 하나씩 적용해보기    
                R, C, S = ele
                dot_result = (R*r)+(C*c)+(S*s)

                if len(result) == output_idx+1: # result에 output_idx에 해당하는 괄호 정보가 아직 기록되어 있지 않으면
                    result.append(dot_result)   # 기록!

                elif result[-1] != dot_result:  # 이미 기록되어 있으면 => 비교해서 다르면 하나로 정의할 수 없는 들여쓰기 횟수 이므로
                    result[-1] = -1             # -1로 다시 기록
                    break
        else:
            result.append(-1)   # 가능한 조합이 없으면  -1 기록
    
    print('#{}'.format(test), *result[:-1])
```



