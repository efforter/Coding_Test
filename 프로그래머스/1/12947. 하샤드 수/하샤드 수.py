def solution(x):
    result = 0
    for i in range(len(str(x))):
        result+=int(str(x)[i])

    if x%result == 0:
        return True
    else:
        return False