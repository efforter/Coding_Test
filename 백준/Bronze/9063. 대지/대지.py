import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if i==0:
        max_x = min_x = a
        max_y = min_y = b
    else:
        if a>max_x:
            max_x = a
        if a<min_x:
            min_x = a
        if b>max_y:
            max_y = b
        if b<min_y:
            min_y = b

print((max_x-min_x)*(max_y-min_y))