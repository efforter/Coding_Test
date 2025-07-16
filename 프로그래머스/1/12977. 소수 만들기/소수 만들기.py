import itertools
from itertools import combinations

def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
    
def solution(nums):
    answer = 0
    ary = list(combinations(nums,3))
    for a in ary:
        if isPrime(sum(a)):
            answer+=1
    return answer