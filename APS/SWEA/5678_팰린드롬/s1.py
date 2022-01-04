import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(1, T+1):

    input_str = input()     # 입려 문자열
    N = len(input_str)      # 입력 문자열 길이

    result = 0
    
    for start_idx in range(N):                          # start_idx: 0 -> N-1
        for end_idx in range(N-1, start_idx-1, -1):     # end_idx: N-1 -> start_idx
            is_palindrom = True                             # 팰린드롬이다! 

            now_start = start_idx
            now_end = end_idx
            while now_start < now_end:
                if input_str[now_start] == input_str[now_end]:  # 같은 문자이면
                    now_start += 1                                  # 다음 문자열 탐색
                    now_end -=1
                else:
                    is_palindrom = False                        # 팰린드롬 아님!
                    break

            if is_palindrom:                            # 팰린드롬이면 
                cnt = end_idx - start_idx + 1               # 팰린드롬인 문자열길이 구해서

                if result < cnt:                        # 가장 긴 팰린드롬 길이 result에 반환
                    result = cnt

    print('#{} {}'.format(test, result))