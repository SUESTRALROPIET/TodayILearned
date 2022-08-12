road = [0 for _ in range(2001)]
road[0] = 1

# road[num]의 경우의 수가 추가될 수 있는 곳은 num+1, num+2 2가지 뿐인 것을 활용
for num in range(2001-2):
    road[num+1] += road[num]
    road[num+2] += road[num]

def solution(n):        
    return road[n] % 1234567