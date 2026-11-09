def solution(n):
    sum = 0
    for i in range(0,n+1):
        if n % 2 == 1:
            sum += i if i % 2 == 1 else 0
        if n % 2 == 0:
            sum += i**2 if i % 2 == 0 else 0
    return sum