import math
n = int(input())
number = list(map(int,input().split()))
sum = 0

for num in number:
    count = 0
    if num == 1:
        continue
    for x in range(2,int(math.sqrt(num))+1):
        if num%x == 0:
            count=1
    if count!=1:
        sum+=1
print(sum)