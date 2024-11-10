import sys
input = sys.stdin.readline

n = int(input())
a,b,c = map(int,input().split())
count = 0
if a<n:
    count+=a
else:
    count+=n
if b<n:
    count+=b
else:
    count+=n
if c<n:
    count+=c
else:
    count+=n
print(count)