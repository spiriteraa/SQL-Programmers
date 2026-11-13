def solution(num_list):
    sum_sq, prod = 0, 1
    for i in num_list:
        prod *= i
        sum_sq += i
    return int(prod < sum_sq**2)