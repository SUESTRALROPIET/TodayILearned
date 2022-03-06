## Lv.2 전화번호 목록

https://programmers.co.kr/learn/courses/30/lessons/42577

#### 1. ~~리스트원소 반복 > 문자열 반복하여 검사~~

> 효율설 3, 4 번 실패 => 시간초과

#### 2. ~~(1번에서 2중 반복문 줄이기)~~

> - 리스트 전체 정렬 후 > 한 번 순회하면서 다음 idx에 있는 원소 체크하기
> - 13번 케이스만 틀림

#### 3. 2번 보완

> `in`을 사용해서 포함여부만 확인하면, 문자열 중간에 포함되어 있어도 체크가 되므로 기준 문자열 길이만큼 비교할 문자열을 슬라이싱해서 비교

```python
def solution(phone_book):
    answer = True
    
    phone_book.sort()   # phone_book 정렬
    N = len(phone_book)
    
    for idx in range(N-1):
        std = phone_book[idx]
        comp = phone_book[idx+1]
        
        if std == comp[:len(std)]:  # std 길이 만큼 comp 앞부분과 비교
            answer = False
            break
    
    return answer
```