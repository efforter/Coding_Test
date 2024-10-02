def solution(arr):
    result = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i-1]==arr[i]:
            continue
        result.append(arr[i])
    return result