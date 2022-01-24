## Lv.2 문자열 압축

https://programmers.co.kr/learn/courses/30/lessons/60057

#### 1. idx를 활용해서 while 반복문으로 해결

```python
def solution(s):
    s_len = len(s)      # input 전체 길이
    part_len = 1        # 단위
    answer = s_len      # answer의 최대값으로 초기화: input 전체 길이

    while part_len <= s_len//2:     # 단위길이: 1 -> input길이//2(최대)
        start = 0       # 시작 idx
        end = part_len  # 끝 idx

        standard = ''   # 기준 문자열
        cnt = 1         # 기준 문자열 개수

        now_result = 0  # 결과값 문자열 길이

        while start < s_len+1:      # start: 0 -> input길이
            if answer <= now_result:
                break

            if not standard:    # 기준 문자열이 없으면
                standard = s[start:end] # 기준 문자열 저장
                start += part_len       # 다음 문자열 탐색을 위한 start & end idx 지정
                end += part_len
                continue

            compare_word = s[start:end] # 비교할 문자열
            if standard == compare_word:    # 기준 문자열 & 비교할 문자열이 같다면
                cnt += 1                        # 문자열 개수 count
                start += part_len               # 다음 문자열 탐색을 위한 start & end idx 지정
                end += part_len
            else:                           # 다르다면
                if cnt == 1:                    # cnt가 1이면, 문자열 길이만 결과값 문자열 길이(now_result)에 더하기
                    now_result += len(standard)
                else:                           # cnt가 1이 아니면, (cnt 길이 + 문자열 길이) 결과값 문자열 길이(now_result)에 더하기
                    now_result += len(str(cnt)) + len(standard)

                standard = ''   # 다음 standard를 구하기 위해 비우고
                cnt = 1         # cnt 초기화

        if standard:    # 남은 비교 문자열 now_result에 더하기
            now_result += len(standard)

        if now_result < answer:     # answer에 최소값 저장
            answer = now_result   

        part_len += 1   # 단위 길이 늘리기

    return answer
```



