import math
def isPrime(k):
    for i in range(2,int(math.sqrt(k))+1):
        if k%i==0:
            return False
    return True

def solution(n):
    count = 0
    for i in range(2,n+1):
        if isPrime(i) == True:
            count+=1
            
    return count