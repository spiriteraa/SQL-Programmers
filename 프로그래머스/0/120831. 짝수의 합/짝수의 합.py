def solution(n):
    return (n/2)*(n/2 + 1) if n % 2 == 0 else ((n-1)/2)*((n-1)/2 + 1)