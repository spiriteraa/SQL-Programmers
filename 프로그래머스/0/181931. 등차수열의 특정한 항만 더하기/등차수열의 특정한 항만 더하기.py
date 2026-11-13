def solution(a, d, included):
    sum = 0
    for i, j in enumerate(included):
        if j:
            sum = sum + a + i*d
    return sum