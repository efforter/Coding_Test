import sys
input = sys.stdin.readline

m = int(input())
temp = 1
for _ in range(m):
    x,y = map(int,input().split())
    if x==temp:
        temp = y
    elif y==temp:
        temp = x
        
print(temp)