import sys
input = sys.stdin.readline

n = int(input())
for i in range(1,n+1):
    print("*"*i+" "*(n-i)*2+"*"*i+" ")

for i in range(n-1,0,-1):
    if i==1:
        print("*"*i+" "*(n-i)*2+"*"*i)
    else:
        print("*"*i+" "*(n-i)*2+"*"*i+" ")