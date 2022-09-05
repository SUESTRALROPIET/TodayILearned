## Lv.3 주차 요금 계산

https://school.programmers.co.kr/learn/courses/30/lessons/92341

#### 1. dictionary자료형 + 조건문 & 반복문
> 시간복잡도: O(N)
>   - 주어진 자료 길이 만큼 반복

```python
    import math

    def solution(fees, records):
        answer = []
        
        # 차량 번호판을 key값으로 갖는 dictionary에 (시간, IN/OUT) 튜플 값 담기
        records_dic = dict()
        for record in records:
            record = record.split(" ")
            if record[1] not in records_dic:
                records_dic[record[1]] = [(record[0], record[2])]
            else:
                records_dic[record[1]].append((record[0], record[2]))
                
        # 번호판 오름차순으로 탐색
        key_lst = list(records_dic.keys())
        key_lst.sort()

        for key in key_lst:
            N = len(records_dic[key])
            max_hr = 23
            max_mi = 59
            total_time = 0

            for idx in range(N-1, -1, -1):      # 뒤에서 부터 탐색
                time, code = records_dic[key][idx]
                time = list(map(int, time.split(":")))
                
                if code == "IN":            # "IN" 코드를 가졌으면 연산 후 total_time에 시간 더하기
                    hr = max_hr - time[0]
                    mi = max_mi - time[1]
                    
                    if mi < 0:
                        mi += 60
                        hr -= 1
                        
                    total_time += (hr * 60)  + mi
                    
                else:                       # "OUT" 코드를 가졌으면 max_hr, max_mi 값 갱신하기
                    max_hr = time[0]
                    max_mi = time[1]
        
            # total_time으로 비용 계산하기
            if total_time - fees[0] <= 0:   
                cost = fees[1]
            else:
                step = (total_time - fees[0]) / fees[2]
                cost = fees[1] + (math.ceil(step) * fees[3])
                
            answer.append(cost)
            
        return answer
```