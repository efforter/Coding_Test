import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

point, count, result = 0, 0, 0

while point < (m - 1):
    if s[point:point + 3] == 'IOI':
        count += 1
        point += 2
        if count == n:
            result += 1
            count -= 1
    else:
        point += 1
        count = 0

print(result)