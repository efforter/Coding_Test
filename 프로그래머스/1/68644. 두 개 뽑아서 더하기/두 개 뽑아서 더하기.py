from itertools import combinations as cb

def solution(numbers):
    ary = list(cb(numbers,2))
    answer = []
    # print(ary)
    for i in range(len(ary)):
        temp = sum(ary[i])
        if not temp in answer:
            answer.append(temp)
    
    answer.sort()
    return answer