def solution(a, b):
    op_1 = str(a)+str(b)
    op_2 = str(b)+str(a)
    return int(max(op_1, op_2))