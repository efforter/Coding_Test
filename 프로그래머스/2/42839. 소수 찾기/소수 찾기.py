from itertools import permutations as pm
import math

def isPrime(number):
    for i in range(2,int(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True
    
def solution(numbers):
    ary = []
    for i in range(1, len(numbers)+1):
        a = pm(numbers,i)
        ary.append(list(set(a)))
        
    result = []
    for i in range(len(ary)):
        for j in range(len(ary[i])):
            temp = ''
            for item in list(ary[i][j]):
                temp += item
            result.append(int(temp))
    
    answer = 0
    for n in list(set(result)):
        if n != 0 and n != 1 and isPrime(n):
            answer += 1
    
    return answer