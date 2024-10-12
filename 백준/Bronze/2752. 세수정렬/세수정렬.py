import sys
input = sys.stdin.readline

ary = list(map(int,input().split()))
ary.sort()
print(*ary)