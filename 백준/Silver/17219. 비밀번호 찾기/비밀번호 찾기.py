import sys
input = sys.stdin.readline

n,m = map(int,input().split())
site = dict()

for _ in range(n):
    s,p = map(str,input().split(' '))
    site[s] = p

for _ in range(m):
    result = input().rstrip()
    print(site[result],end='')