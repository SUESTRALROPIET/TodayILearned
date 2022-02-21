## 사전학습

1. 다중 합집합 / 교집합

   https://velog.io/@munang/%EA%B0%9C%EB%85%90%EC%A0%95%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8B%A4%EC%A4%91-%EC%A7%91%ED%95%A9

   

## Lv.2 뉴스 클러스터링

https://programmers.co.kr/learn/courses/30/lessons/17677

#### 1. 다중집합 합집합/교집합 구현

> - 다중집합 합집합/교집합 구현 시, 
>   - 중복된 원소 포함 여부 주의
>   - 얕은 복사가 되지 않도록 주의! 

```python
def solution(str1, str2):
    def make_lst(input_str):
        return_lst = []
        N = len(input_str)
        for input_idx in range(N-1):
            if input_str[input_idx:input_idx+2].isalpha():          # 알파벳일 경우만
                return_lst.append(input_str[input_idx:input_idx+2].upper())     # 대문자로 변환해서 return_lst에 추가
        return return_lst

    # 길이가 2인 문자열로 나누기
    str1_lst = make_lst(str1)
    str2_lst = make_lst(str2)
    
    compare1 = []   # 다중집합 교집합
    compare1_1 = [] 
    compare2 = []   # 다중집합 합집합
    compare2_1 = []

    compare1_1 += str2_lst      # 다중집합 교집합 초기화
    compare2 += str1_lst        # 다중집합 합집합 초기화
    compare2_1 += str1_lst      # 다중집합 합집합 초기화

    # 다중집합 교집합 만들기
    for str1_ele in str1_lst:           # 집합1을 반복
        if str1_ele in compare1_1:      # 집합2가 담긴 compare1_1에 집합1 원소가 있다면
            compare1.append(str1_ele)       # 다중집합 교집합에 추가
                                            # 추가: 4, 7, 9, 10, 11 틀림
            compare1_1.remove(str1_ele)     # 집합2가 담긴 compare1_1에서 제거(탐색 시, 더 이상 공통원소가 아님을 체크하기 위해)

    # 다중집합 합집합 만들기 (compare2에는 집합1 원소가 있는 상태)
    for str2_ele in str2_lst:           # 집합2를 반복
        if not str2_ele in compare2_1:  # 집합1이 담긴 compare2_1에 집합2 원소가 없으면
            compare2.append(str2_ele)       # compare2(다중집합 합집합)에 원소 추가
        else:                           # 원소가 있으면
            compare2_1.remove(str2_ele)     # compare2_1에서 해당 원소 제거(값이 같은 원소가 있는 경우 추가할 수 있도록 체크하기 위해)
    
    try:
        answer = len(compare1) / len(compare2) * 65536      # 일단 계산하고
    except:
        answer = 1 * 65536                                  # Zero Division Error가 생기면 기본값 반환

    return int(answer)
```



