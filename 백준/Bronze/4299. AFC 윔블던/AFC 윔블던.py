import sys
input = sys.stdin.readline

a,b = map(int,input().split())
if a+b<0 or a-b<0 or (a+b)%2:
    print(-1)
else:
    print((a+b)//2,a-(a+b)//2)