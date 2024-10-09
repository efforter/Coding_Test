import math
def solution(n):
    count = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            if i==(n//i):
                count += i
            else:
                count += i+(n//i)
            
    return count