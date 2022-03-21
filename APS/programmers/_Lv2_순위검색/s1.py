def solution(info, query):
    query_len = len(query)
    answer = [0] * query_len

    jobseekers = []
    hrs = []

    for ele in info:
        jobseekers.append(list(ele.split()))
    for ele in query:
        hrs.append(list(ele.split(' and ')))
        
        
    for idx, hr in enumerate(hrs):
        for jobseeker in jobseekers:
            for con_idx in range(4):
                if con_idx == 3:
                    food, score = hr[con_idx].split()
                    if (food == '-' or jobseeker[con_idx] == food) and int(score) <= int(jobseeker[4]):
                        answer[idx] += 1
                if hr[con_idx] == '-' or jobseeker[con_idx] == hr[con_idx]:
                    continue
                else:
                    break        
    return answer
