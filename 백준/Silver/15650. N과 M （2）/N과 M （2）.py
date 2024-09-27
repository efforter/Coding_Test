import sys
input = sys.stdin.readline

def DFS(x):
    if len(seq)==m:
        print(*seq)
        return
    
    for i in range(x,n+1):
        if i not in seq:
            seq.append(i)
            DFS(i)
            seq.pop()

n,m = map(int,input().split())
seq = []

DFS(1)