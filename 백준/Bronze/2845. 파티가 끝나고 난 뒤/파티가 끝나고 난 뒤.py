import sys
input = sys.stdin.readline

l,p = map(int,input().split())
temp = l*p
ary = list(map(int,input().split()))
for a in ary:
    print(a-temp,end=' ')