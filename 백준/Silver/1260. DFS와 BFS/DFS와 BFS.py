import sys
input = sys.stdin.readline
from collections import deque

def DFS(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)

def BFS(graph,v,visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        x = queue.popleft()
        print(x,end=' ')

        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

DFS(graph,v,visited)
print("")
visited = [False] * (n+1)
BFS(graph,v,visited)