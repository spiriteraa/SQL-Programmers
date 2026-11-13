def solution(num_list):
    odd_str = ''
    ev_str = ''
    for i, c in enumerate(num_list):
        if c % 2 == 0:
            ev_str += str(num_list[i])
        else:
            odd_str += str(num_list[i])
    return int(ev_str) + int(odd_str)