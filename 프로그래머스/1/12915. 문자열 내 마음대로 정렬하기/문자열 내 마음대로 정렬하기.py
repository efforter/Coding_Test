def solution(strings, n):
    ary = []
    for s in strings:
        ary.append([s[n],s])
    ary.sort()
    result = []
    for i in range(len(strings)):
        result.append(ary[i][1])
    return result