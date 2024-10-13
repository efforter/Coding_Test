def solution(n):
    temp = 10
    ary = []
    for i in range(len(str(n))):
        ary.append((n%temp)//(temp//10))
        temp *= 10

    return ary