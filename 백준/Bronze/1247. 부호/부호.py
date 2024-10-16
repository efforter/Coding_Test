import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    count = 0
    for i in range(n):
        count += int(input())
    if count==0:
        print(0)
    elif count>0:
        print("+")
    else:
        print("-")