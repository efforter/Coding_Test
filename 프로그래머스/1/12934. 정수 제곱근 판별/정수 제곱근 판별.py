import math
def solution(n):
    v = math.sqrt(n)
    if pow(int(v),2)==n:
        return pow(int(v)+1,2)
    else:
        return -1