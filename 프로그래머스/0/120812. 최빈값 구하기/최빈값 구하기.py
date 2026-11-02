import collections

def solution(array):
    count = collections.Counter(array).most_common()
    if len(count) == 1:
        return count[0][0]
    else:
        if count[0][1] == count[1][1]:
            return -1
        else:
            return count[0][0]