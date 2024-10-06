import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
count = 0
if a==b==c:
    count = 10000+a*1000
elif a==b:
    count = 1000+a*100
elif b==c:
    count = 1000+b*100
elif a==c:
    count = 1000+a*100
else:
    count = max(a,b,c)*100
print(count)