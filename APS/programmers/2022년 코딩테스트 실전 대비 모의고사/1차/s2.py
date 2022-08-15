def solution(want, number, discount):
    answer = 0

    N = len(want)
    D = len(discount)

    for dis_idx in range(0, D-10+1):
        dis = discount[dis_idx:dis_idx+10]
        status = 0
        for ele_idx in range(N):
            cnt = dis.count(want[ele_idx])
            if cnt == number[ele_idx]:
                status += 1
            else:
                break
        if status == N:
            answer += 1

    return answer