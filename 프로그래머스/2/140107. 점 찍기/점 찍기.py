import math

def solution(k, d):
    answer = 0
    for x in range(0, d+1, k):
        max = math.floor(math.sqrt(d**2 - x**2))
        answer += math.floor(max/k) + 1
    return answer