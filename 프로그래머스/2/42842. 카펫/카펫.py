import math
'''
26 10
36 = 1,2,3,4,6,9,12,18,36
(6-2)*(6-2) = 16
(4-2)*(9-2) = 14
(3-2)*(12-2) = 10
'''
def solution(brown, yellow):
    temp = int(math.sqrt(brown+yellow))
    for i in range(temp,2,-1):
        if (brown+yellow)%i==0:
            if ((brown+yellow)//i-2) * (i-2) == yellow:
                return (brown+yellow)//i,i