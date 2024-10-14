import sys
input = sys.stdin.readline
import math

n = int(input())
num = [math.pow(i,2) for i in range(1,224)]
if n in num:
    print(1)
    exit()

for i in range(1, int(math.sqrt(n))+1):
    if (n-math.pow(i,2)) in num:
        print(2)
        exit()

for i in range(1, int(math.sqrt(n))+1):
    for j in range(1, int(math.sqrt(n))+1):
        if (n-math.pow(i,2)-math.pow(j,2)) in num:
            print(3)
            exit()
print(4)