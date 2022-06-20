import itertools

def solution(number, k):
    N = len(number)
    
    elements = list(itertools.combinations(number, N-k))
    elements.sort()
    answer = ''.join(elements[-1])

    return answer