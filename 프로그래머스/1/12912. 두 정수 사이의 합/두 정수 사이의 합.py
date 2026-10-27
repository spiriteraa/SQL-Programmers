def solution(a, b):
    answer = 0
    if a < b:
        i = a
        while i <= b:
            answer += i
            i += 1
    elif a == b:
        answer = a
    elif a > b:
        i = b
        while i <= a:
            answer += i
            i += 1
    return answer