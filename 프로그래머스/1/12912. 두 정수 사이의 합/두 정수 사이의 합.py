def solution(a, b):
    x = min(a,b)
    y = max(a,b)
    temp = 0
    for i in range(x,y+1):
        temp += i
    return temp