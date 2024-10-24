import sys
input = sys.stdin.readline

n = int(input())
ary = list(map(int,input().split()))
v = int(input())

count = 0
for x in ary:
    if x==v:
        count+=1
print(count)