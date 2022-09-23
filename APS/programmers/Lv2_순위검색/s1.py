def solution(info, query):
    answer = []
    
    N = len(info)
    for idx in range(N):
        info[idx] = info[idx].split(' ')
    
    for query_str in query:
        checked = [True for _ in range(N)]
        ele_idx = 0
        for query_ele in query_str.split(' '):
            if ele_idx > 5:
                break
            if query_ele == 'and':
                continue
            if query_ele == '-':
                ele_idx += 1
                continue
            for info_idx in range(N):
                if not checked[info_idx]:
                    continue
                if ele_idx == 4:
                    if int(query_ele) > int(info[info_idx][ele_idx]):
                        checked[info_idx] = False
                    continue
                if query_ele != info[info_idx][ele_idx]:
                    checked[info_idx] = False
            ele_idx += 1
        answer.append(sum(checked))
    return answer