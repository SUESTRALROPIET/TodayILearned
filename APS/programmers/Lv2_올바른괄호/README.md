## Lv.2 올바른 괄호

https://school.programmers.co.kr/learn/courses/30/lessons/12909

#### 1. dictionary 자료형 & 반복문 활용
> 시간복잡도: O(파일길이) => O(N)

 ```python
  def solution(s):
      answer = True
      cnt_dic = {'(': 0, ')': 0}
      
      for ele in s:
          cnt_dic[ele] += 1
          
          if cnt_dic['('] < cnt_dic[')']:     # 오른쪽 괄호가 넘치면 => False
              return False  

      if cnt_dic['('] > cnt_dic[')']:    # 왼쪽 괄호가 넘치면 => False
          return False
      
      return True
 ```