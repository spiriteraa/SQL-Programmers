def solution(a, b, c):
    if abs((a-b))+abs((b-c))+abs((c-a)) == 0:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    else:
        if abs((a-b)*(b-c))*abs((b-a)*(a-c))*abs((a-c)*(c-b)) == 0:
            return (a+b+c)*(a**2+b**2+c**2)
        else:
            return a+b+c