def solution(a, b):
    op_1 = str(a)+str(b)
    op_2 = str(b)+str(a)
    return int(op_1) if op_1 >= op_2 else int(op_2)