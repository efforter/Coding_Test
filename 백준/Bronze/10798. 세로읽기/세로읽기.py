import sys
input = sys.stdin.readline

ary = []
temp = 0
for _ in range(5):
    a = list(input().rstrip())
    ary.append(a)
    if len(a) > temp:
        temp = len(a)

for i in range(temp):
    for s in ary:
        if s:
            print(s[0],end='')
            del s[0]