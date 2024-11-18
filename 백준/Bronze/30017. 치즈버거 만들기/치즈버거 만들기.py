import sys
input = sys.stdin.readline

a,b = map(int,input().split())

if b>=a:
    b = a-1

if a>=b+1:
    a = b+1
print(a+b)