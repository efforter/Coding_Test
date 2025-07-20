import math

def solution(left, right):
    answer=0
    for num in range(left,right+1):
        result = 0
        if num==1:
            result+=1
        else:
            for n in range(1,int(math.sqrt(num))+1):
                if num%n==0:
                    if n**2==num:
                        result+=1
                    else:
                        result+=2
        if result%2==0:
            answer += num
        else:
            answer -= num
    return answer