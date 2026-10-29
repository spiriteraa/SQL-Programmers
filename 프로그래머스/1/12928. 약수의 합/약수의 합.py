import math

def solution(n):
    answer = 0
    i = 1;
    while i < math.sqrt(n):
        if n % i == 0:
            answer = answer + i + n/i
        i += 1
    if i == math.sqrt(n):
        answer += i
    return answer