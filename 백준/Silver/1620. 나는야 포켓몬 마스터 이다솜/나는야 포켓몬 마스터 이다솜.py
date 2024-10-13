import sys
input = sys.stdin.readline

n,m = map(int,input().split())
voca_s = dict()
voca_n = dict()
for i in range(n):
    s = input().rstrip()
    voca_s[i+1] = s
    voca_n[s] = i+1

for _ in range(m):
    s = input().rstrip()
    if s.isdigit():
        print(voca_s[int(s)])
    else:
        print(voca_n[s])