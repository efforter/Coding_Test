from itertools import combinations as cb

def solution(number):
    a = list(cb(number,3))
    print(a)
    answer = 0
    
    for i in a:
        if sum(i) == 0:
            answer += 1
    return answer