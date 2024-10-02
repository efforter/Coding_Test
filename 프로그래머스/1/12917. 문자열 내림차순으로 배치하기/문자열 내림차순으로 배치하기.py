def solution(s):
    low = []
    upp = []
    for x in s:
        if x.islower()==1:
            low.append(x)
        else:
            upp.append(x)
    low.sort(reverse=True)
    upp.sort(reverse=True)
    result = ''
    for x in low:
        result += x
    for x in upp:
        result += x
    return result