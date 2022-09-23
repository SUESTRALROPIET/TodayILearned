## Lv.2 순위 검색

https://school.programmers.co.kr/learn/courses/30/lessons/72412

#### 1. 단순 반복문
> 효율성 테스트: 시간초과

> 시간복잡도: O(N * M * 5)
>   - N: query 길이
>   - M: info 길이
>   - 5: info 요소 총 길이


#### 2. info가 가능한 경우의 수 미리 dict에 담고 > 해당 value값 리스트에서 해당하는 값의 개수 반환하기
> [참고 풀이](https://school.programmers.co.kr/questions/27140)

> 시간복잡도: O(N * log M)
>   - N: query 길이
>   - M: query에 해당하는 value값 리스트 길이


```python
  def solution(info, query):
      answer = []

      # 가능한 경우의 수를 key값으로, score을 value값으로 갖기
      info_dict = dict()
      for single_info in info:
          info_lst = single_info.split(' ')
          score = int(info_lst[4])
          for lang in ["-", info_lst[0]]:
              for part in ["-", info_lst[1]]:
                  for level in ["-", info_lst[2]]:
                      for food in ["-", info_lst[3]]:
                          info_key = lang + part + level + food
                          if info_key in info_dict:
                              info_dict[info_key].append(score)
                          else:
                              info_dict[info_key] = [score]
      
      # 각 key의 value값 정렬 => 시간초과 문제 해결 포인트
      for key in info_dict.keys():
          info_dict[key].sort()

      # query_str을 key값으로 갖는 value 리스트에서 
      # 해당하는 원소들의 개수 이진탐색으로 추출하기
      for query_str in query:
          query_lst = query_str.split(" ")
          condition = ''.join(query_lst[:-1])
          condition = condition.replace("and", "")

          if condition in info_dict:
              value_lst = info_dict[condition]
          else:
              value_lst = []
              
          N = len(value_lst)
          target = int(query_lst[-1])
          
          start = 0
          end = N

          while start < end:
              mid = (start + end) // 2

              if target <= value_lst[mid]:
                  end = mid

              else:
                  start = mid + 1
          
          answer.append(N - end)

      return answer
```