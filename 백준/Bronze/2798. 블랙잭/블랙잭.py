n,m = map(int,input().split())
ary = list(map(int,input().split()))
sum = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if ary[i] + ary[j] + ary[k] <= m:
                sum = max(sum,ary[i] + ary[j] + ary[k])
print(sum)