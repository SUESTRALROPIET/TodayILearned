def solution(progresses, speeds):
    answer = []
    
    N = len(progresses)     # 작업 개수
    num_lst = [0] * N       # 작업에 필요한 시간을 담을 리스트 초기화
    
    date = 0    # 날짜 초기화
    
    for idx in range(N):
        quotient, remainder = divmod(100-progresses[idx], speeds[idx])  # 남은 작업량 / 개발속도

        num_lst[idx] = quotient     # 작업에 필요한 시간 = 몫 or 나머지가 있다면 하루 추가
        if remainder: 
            num_lst[idx] += 1

        if num_lst[idx] <= date:    # date보다 작거나 같으면 함께 배포
            answer[-1] += 1
            continue
        else:                       # date보다 필요한 날짜가 크면
            date = num_lst[idx]         # 개발에 필요한 날짜만큼 date를 업데이트하고
            answer.append(1)            # 배포할 것임을 표시
    return answer

