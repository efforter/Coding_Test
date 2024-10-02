def solution(arr, divisor):
    result = []
    for x in arr:
        if x%divisor==0:
            result.append(x)
    if result:
        result.sort()
    else:
        result.append(-1)
    return result