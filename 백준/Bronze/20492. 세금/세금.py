import sys
input = sys.stdin.readline

n = int(input())

a = n//100*78
b = n-n//100*20//100*22
print(a,b)