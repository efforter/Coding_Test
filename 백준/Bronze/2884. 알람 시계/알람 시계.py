h,m = map(int, input().split())
sum = h*60 + m - 45
if sum < 0:
    sum+=1440
print(int(sum/60), sum%60)