import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(graph,v,visited):
    visitied[v] = True

    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visitied = [False] * (n+1)
count = 0
for i in range(1,n+1):
    if not visitied[i]:
        DFS(graph,i,visitied)
        count += 1

print(count)