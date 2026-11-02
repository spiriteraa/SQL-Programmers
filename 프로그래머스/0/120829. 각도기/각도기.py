import math

def solution(angle):
    return math.floor(angle/90)*2+1 if angle%90 != 0 else angle/90 * 2