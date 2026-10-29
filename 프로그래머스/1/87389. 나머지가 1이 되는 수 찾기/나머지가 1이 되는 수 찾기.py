def solution(n):
    i = 2
    while (n - 1) % i != 0:
        i += 1
    return i