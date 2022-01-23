def solution(s):
    s_len = len(s)
    part_len = 1
    answer = s_len

    while part_len <= s_len//2:
        start = 0
        end = part_len
        standard = ''
        cnt = 1
        now_result = 0
        while start < s_len:
            if answer <= now_result:
                break

            if not standard:
                standard = s[start:end]
                start += part_len
                end += part_len
                continue

            compare_word = s[start:end]
            if standard == compare_word:
                cnt += 1
                start += part_len
                end += part_len
            else:
                if cnt == 1:
                    now_result += len(standard)
                else:
                    now_result += len(str(cnt)) + len(standard)

                standard = ''
                cnt = 1

        if cnt == 1:
            now_result += len(standard)
        else:
            now_result += len(str(cnt)) + len(standard)    

        if now_result < answer:
            answer = now_result        
        part_len += 1

    return answer
