import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(x):
    for i in tree[x]:
        if not visited[i]:
            visited[i] = x
            DFS(i)

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

DFS(1)

for i in range(2,n+1):
    print(visited[i])