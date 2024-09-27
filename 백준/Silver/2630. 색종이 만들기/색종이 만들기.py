import sys
input = sys.stdin.readline

def cut(a,b,n):
    global count_0, count_1
    temp = color[a][b]
    for i in range(a,a+n):
        for j in range(b,b+n):
            if color[i][j] != temp:
                m = n//2
                cut(a,b,m)
                cut(a,b+m,m)
                cut(a+m,b,m)
                cut(a+m,b+m,m)
                return
    if temp == 0:
        count_0 += 1
    else:
        count_1 += 1

n = int(input())
color = [list(map(int,input().split())) for _ in range(n)]
count_0 = count_1 = 0
cut(0,0,n)
print(count_0)
print(count_1)