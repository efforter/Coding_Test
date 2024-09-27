import sys
input = sys.stdin.readline

def DFS(x):
    if len(seq)==m:
        print(*seq)
        return
    
    for i in res:
        if i not in seq:
            seq.append(i)
            DFS(i)
            seq.pop()

n,m = map(int,input().split())
res = list(map(int,input().split()))
res.sort()
seq = []

DFS(1)