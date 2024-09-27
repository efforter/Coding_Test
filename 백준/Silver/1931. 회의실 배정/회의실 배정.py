import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
conf = [list(map(int,input().split())) for _ in range(n)]
conf.sort(key=lambda x:(x[1],x[0]))

temp = count = 0

for a,b in conf:
    if a >= temp:
        count += 1
        temp = b

print(count)