n = int(input())
card = list(map(int,input().split()))
card.sort()
m = int(input())
number = list(map(int,input().split()))

dic = {}

for c in card:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1

for x in number:
    if x in dic:
        print(dic[x], end=' ')
    else:
        print('0', end=' ')