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


a = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]	
print(solution(a, b))