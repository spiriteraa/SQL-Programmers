def solution(angle):
    return (angle//90)*2+1 if angle%90 != 0 else angle/90 * 2